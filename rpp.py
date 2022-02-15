#-----------------------------------------------------------------------------
# rpp.py
# RenPy processor classes
# pylint: disable=bad-indentation
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
class RenPyLabelCall():
  def __init__(self, l, v):
    #type: (str, dict[str, str]) -> None
    self.label = l;
    self.vars  = v;

  def __repr__(self):
    #type: () -> str
    return(self.label + ", " + str(self.vars));

  def __eq__(self, other):
    #type: (RenPyLabelCall) -> bool
    return self.vars == other.vars and self.label == other.label;

#-----------------------------------------------------------------------------
class RenPyObject():
  def __init__(self, ln, ind):
    #type: (int, int) -> None
    self.objType = "Object";
    self.done    = False;
    self.lineNum = ln;
    self.indent  = ind;

#-----------------------------------------------------------------------------
class RenPyBlock(RenPyObject):
  def __init__(self, ln, ind):
    #type: (int, int) -> None
    super().__init__(ln, ind);
    self.objType = "Block";

  def __repr__(self):
    #type: () -> str
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
    #type: (dict[str,str], list[RenPyObject]) -> None
    self.vars  = v;
    self.stack = s;

  def __eq__(self, other):
    #type: (RenPyThread) -> bool
    return self.vars == other.vars and self.stack == other.stack;

#-----------------------------------------------------------------------------
class RenPyFile():
  def __init__(self):
    self.lines     = [] #type: list[str]
    self.numLines  = 0
    self.labelList = {} #type: dict[str, int]
    self.backMap   = {} #type: dict[str, str]
    self.charMap   = {} #type: dict[str, dict[str,str]]
    self.v6Map     = {} #type: dict[str, dict[str,str]]
    self.charFlip  = [] #type: list[str]
    self.visLines  = [] #type: list[int]
    self.showLines = [] #type: list[int]
    self.trackVis  = False;
    self.lineModifiedFlags = {} #type: dict[int, bool]

  def readFile(self, fn):
    #type: (str) -> None
    text_file = open(fn, "r", encoding="utf8");
    self.lines = text_file.readlines();
    self.numLines = len(self.lines);

  def writeFile(self, fn):
    #type: (str) -> None
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
          if self.labelIsAcceptable(label):
            self.labelList[label] = i;
      i = i + 1;

  def indentIsGood(self, lineNum, indent):
    #type: (int, int) -> bool
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
    #type: (int, int) -> int
    i = lineNum;
    while(i < self.numLines):
      if (not(self.indentIsGood(i, indent))):
        return i;
      i = i + 1;
    return i;

  def getIndentOf(self, line):
    #type: (str) -> int
    indent = 0;
    lineLen = len(line);

    while((indent < lineLen) and (line[indent] == ' ')):
      indent = indent + 1;
    return indent;

  # Ensures a 'show' line has an 'xzoom' instruction
  # Existing xzoom isn't changed, missing gets xzoom 1
  def addXZoom(self, lineNum):
    #type: (int) -> None
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
      strippedLine = self.lines[lineNum].strip();
      if (strippedLine.startswith("show")):
        self.reverseXZoom(lineNum);
    self.numLines = len(self.lines);

  # Reverses an xzoom line in a 'show' statement
  def reverseXZoom(self, lineNum):
    #type: (int) -> None
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
    #type: (str) -> bool
    return True;

  def hookIf(self, thread):
    #type: (RenPyThread) -> None
    pass;

  def processCG(self, line):
    #type: (str) -> str
    return line;

  def addMutators(self, charName):
    #type: (str) -> str
    return charName;

#-----------------------------------------------------------------------------
class RenPyFileCiel(RenPyFile):
  def __init__(self, b, c, v6):
    #type: (dict[str, str], dict[str, dict[str,str]], dict[str, dict[str,str]]) -> None
    super().__init__();
    self.backMap = b;
    self.charMap = c;
    self.v6Map = v6;
    self.charFlip = ["main", "mother", "nick"];
    self.trackVis = True;

  def readFile(self, fn):
    #type: (str) -> None
    super().readFile(fn);

    # Patch the initial hide of Calvin
    self.lines[5] = "    hide maind\n";

  def addMutators(self, charName):
    #type: (str) -> str
    if (charName == "ciel"):
      return "ciel hair headband";
    return charName;

#-----------------------------------------------------------------------------
class RenPyFileEliza(RenPyFile):
  def __init__(self, b, c, v6):
    #type: (dict[str, str], dict[str, dict[str,str]], dict[str, dict[str,str]]) -> None
    super().__init__();
    self.backMap = b;
    self.charMap = c;
    self.v6Map = v6;

  def readFile(self, fn):
    #type: (str) -> None
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

    # Rename Jillian's "maid opened" base to "maidop"
    self.lines[25654] = self.lines[25654].replace("maid opened", "maidop");
    self.lines[25657] = self.lines[25657].replace("maid opened", "maidop");
    self.lines[25660] = self.lines[25660].replace("maid opened", "maidop");

  def labelIsAcceptable(self, label):
    #type: (str) -> bool  
    if ("goopy" in label):
      return False;
    if (label == "kpathendroundup2"):
      return False;
    if label.startswith("endingclone"):
      return False;
    return True;

  def hookIf(self, thread):
    #type: (RenPyThread) -> None
    # Short-circuit the recursion in the joke Christine endings
    obj = thread.stack[-1];
    if (obj.lineNum == 10181):
      thread.vars["JokeEnding"] = "5";

#-----------------------------------------------------------------------------
class RenPyFileGoopy(RenPyFile):
  def __init__(self, b, c, v6):
    #type: (dict[str, str], dict[str, dict[str,str]], dict[str, dict[str,str]]) -> None
    super().__init__();
    self.backMap = b;
    self.charMap = c;
    self.v6Map = v6;
    self.charFlip = ["main", "mother", "nick"];
    self.trackVis = True;

  def readFile(self, fn):
    #type: (str) -> None
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
    #type: (str) -> str
    fields = line.strip().strip(":").split();
    fields[1] = "cgex";
    rv = (" " * self.getIndentOf(line)) + " ".join(fields);
    if ":" in line:
      rv += ":";
    return rv + "\n";

  def addMutators(self, charName):
    #type: (str) -> str
    if (charName == "ciel"):
      return "ciel hair headband";
    return charName;
