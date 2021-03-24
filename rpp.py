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

