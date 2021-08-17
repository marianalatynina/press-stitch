#-----------------------------------------------------------------------------
# rpp.py
# RenPy processor classes
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
class RenPyLabelCall():
  def __init__(self, l, v):
    self.label = l;
    self.vars  = v;

  def __repr__(self):
    return(self.label + ", " + str(self.vars));

  def __eq__(self, other):
    return self.vars == other.vars and self.label == other.label;

#-----------------------------------------------------------------------------
class RenPyObject():
  def __init__(self, ln, ind):
    self.objType = "Object";
    self.done    = False;
    self.lineNum = ln;
    self.indent  = ind;

#-----------------------------------------------------------------------------
class RenPyBlock(RenPyObject):
  def __init__(self, ln, ind):
    super().__init__(ln, ind);
    self.objType = "Block";

  def __repr__(self):
    return("blk(" + str(self.lineNum) + "," + str(self.indent) + ")");

#-----------------------------------------------------------------------------
class RenPyIf(RenPyObject):
  def __init__(self, ln, ind):
    super().__init__(ln, ind);
    self.objType = "If";
    self.hasExecuted = False;

  def __repr__(self):
    return("if(" + str(self.lineNum) + "," + str(self.indent) + ")");

#-----------------------------------------------------------------------------
class RenPyThread():
  def __init__(self, v, s):
    self.vars  = v;
    self.stack = s;

  def __eq__(self, other):
    return self.vars == other.vars and self.stack == other.stack;

#-----------------------------------------------------------------------------
class RenPyFile():
  def __init__(self):
    self.lines     = [];
    self.numLines  = 0;
    self.labelList = {};
    self.backMap   = {};
    self.charMap   = {};
    self.v6Map     = {};
    self.charFlip  = [];
    self.visLines  = [];
    self.showLines = [];
    self.trackVis  = False;
    self.lineModifiedFlags = {};

  def readFile(self, fn):
    text_file = open(fn, "r", encoding="utf8");
    self.lines = text_file.readlines();
    self.numLines = len(self.lines);

  def writeFile(self, fn):
    with open(fn, "w", encoding="utf8") as outfile:
      outfile.writelines(self.lines);

  def findLabels(self):
    i = 0;
    strippedLine = "";
    while i < self.numLines:
      strippedLine = self.lines[i].strip();
      if strippedLine.startswith("label"):
        fields = strippedLine.strip(":").split();
        if (fields[0] == "label"):
          label = fields[1];
          self.labelList[label] = i;
      i = i + 1;

  def indentIsGood(self, lineNum, indent):
    i = 0;
    line = self.lines[lineNum];
    lineLen = len(line);
    while(i < lineLen):
      if (i == indent):
        return True;
      if ((line[i] != ' ') and (line[i] != '\r') and (line[i] != '\n')):
        return False;
      i = i + 1;

    # Line is shorter than indent with no characters, this is fine
    return True;

  def blockEndLine(self, lineNum, indent):
    i = lineNum;
    while(i < self.numLines):
      if (not(self.indentIsGood(i, indent))):
        return i;
      i = i + 1;
    return i;

  def getIndentOf(self, line):
    indent = 0;
    lineLen = len(line);

    while((indent < lineLen) and (line[indent] == ' ')):
      indent = indent + 1;
    return indent;

  # Ensures a 'show' line has an 'xzoom' instruction
  # Existing xzoom isn't changed, missing gets xzoom 1
  def addXZoom(self, lineNum):
    line = self.lines[lineNum];
    fields = line.strip().strip(":").split();
    if (fields[1] == "bg"):
      return;
    if not(fields[1] in self.charFlip):
      return;

    indent = self.getIndentOf(line) + 4;
    if not(line.strip()[-1] == ':'):
      self.lines[lineNum] = line.strip('\n').strip('\r') + ":\n";
      self.lines.insert(lineNum + 1, (" " * indent) + "xzoom 1\n");
      return;

    # The character has following lines
    lineNum += 1;
    insertLineNum = lineNum;
    line = self.lines[lineNum];
    while (lineNum < self.numLines) and (self.getIndentOf(line) == indent):
      if (line.strip().startswith("xzoom ")):
        return;
      lineNum += 1;
      line = self.lines[lineNum];

    # Need to insert
    self.lines.insert(insertLineNum, (" " * indent) + "xzoom 1\n");

  # Flip all V3 affected characters left-to-right
  def doFlips(self):
    for lineNum in sorted(self.visLines, reverse=True):
      self.addXZoom(lineNum);
    self.numLines = len(self.lines);

    # Reverse all xzoom calls for affected characters
    for i in self.showLines:
      strippedLine = self.lines[i].strip();
      if (strippedLine.startswith("show")):
        self.reverseXZoom(i);
      i = i + 1;

  # Reverses an xzoom line in a 'show' statement
  def reverseXZoom(self, lineNum):
    line = self.lines[lineNum];
    fields = line.strip().strip(":").split();
    if (fields[1] == "bg"):
      return;
    if not(fields[1] in self.charFlip):
      return;
    if not(line.strip()[-1] == ':'):
      return;

    # The character has following lines
    indent = self.getIndentOf(line) + 4;
    lineNum += 1;
    line = self.lines[lineNum];
    while (lineNum < self.numLines) and (self.getIndentOf(line) == indent):
      if (line.strip().startswith("xzoom -1")):
        self.lines[lineNum] = (" " * indent) + "xzoom 1\n";
        return;
      if (line.strip().startswith("xzoom 1")):
        self.lines[lineNum] = (" " * indent) + "xzoom -1\n";
        return;
      lineNum += 1;
      line = self.lines[lineNum];

  def findShows(self):
    i = 0;
    self.lineModifiedFlags = {};
    while i < self.numLines:
      strippedLine = self.lines[i].strip();
      if (strippedLine.startswith("show") or strippedLine.startswith("scene")):
        self.lineModifiedFlags[i] = False;
      i = i + 1;

  def labelIsAcceptable(self, label):
    return True;

  def hookIf(self, thread):
    pass;

  def processCG(self, line):
    return line;

#-----------------------------------------------------------------------------
class RenPyFileCiel(RenPyFile):
  def __init__(self, b, c, v6):
    super().__init__();
    self.backMap = b;
    self.charMap = c;
    self.v6Map = v6;
    self.charFlip = ["main", "mother", "nick"];
    self.trackVis = True;

  def readFile(self, fn):
    super().readFile(fn);

    # Patch the initial hide of Calvin
    self.lines[5] = "    hide maind\n";

#-----------------------------------------------------------------------------
class RenPyFileEliza(RenPyFile):
  def __init__(self, b, c, v6):
    super().__init__();
    self.backMap = b;
    self.charMap = c;
    self.v6Map = v6;

  def readFile(self, fn):
    super().readFile(fn);

    # Patch the timer
    self.lines[6396] = (" " * 20) + "if timer_value >= 30:\n";
    self.lines[6552] = (" " * 20) + "if timer_value >= 30:\n";
    self.lines[6713] = (" " * 20) + "if timer_value >= 30:\n";

    # Patch the "Karyn" if switched menu option in kpathendroundup
    self.lines[68980] = "            jump kpathendroundup2\n";

    # Patch Michelle's age
    self.lines[587] = self.lines[587].replace("14", "15");
    self.lines[589] = self.lines[589].replace("14", "15");

  def labelIsAcceptable(self, label):
    return not("goopy" in label);

  def hookIf(self, thread):
    # Short-circuit the recursion in the joke Christine endings
    obj = thread.stack[-1];
    if (obj.lineNum == 10181):
      thread.vars["JokeEnding"] = "5";

#-----------------------------------------------------------------------------
class RenPyFileGoopy(RenPyFile):
  def __init__(self, b, c, v6):
    super().__init__();
    self.backMap = b;
    self.charMap = c;
    self.v6Map = v6;
    self.charFlip = ["main", "mother", "nick"];
    self.trackVis = True;

  def readFile(self, fn):
    super().readFile(fn);

    # Patch the menu to enable the Goopy path
    self.lines[85] = "        \"Tried to become a clone of her.\":\n";
    self.lines[86] = "\n";
    self.lines[87] = "\n";
    self.lines[89] = "\n";

    # Make sure 'maind' displayable is hidden on entry
    self.lines.insert(69381, "        hide maind\n");
    self.numLines = len(self.lines);

    # Alter the Eliza bed CG
    self.lines[69698] = "                scene cgbase eliza sleep 1\n";
    self.lines[69699] = "                show cgex eliza sleep 1\n";

    # The Eliza H pic is missing in 0.5, patch it out
    self.lines[69774] = "                        show cgex eliza sleep 6\n";
    self.lines[69775] = "\n";

  def processCG(self, line):
    fields = line.strip().strip(":").split();
    fields[1] = "cgex";
    rv = (" " * self.getIndentOf(line)) + " ".join(fields);
    if ":" in line:
      rv += ":";
    return rv + "\n";
