#-----------------------------------------------------------------------------
# press-stitch.py
# Merges the three Press Switch games together
#-----------------------------------------------------------------------------

import getopt
import hashlib
import os.path
import pathlib
import shutil
import sys
import zipfile
import press_stitch_archive

filename_03 = "Press-SwitchV0.3b-all";
filename_04 = "Press-SwitchV0.4a-pc";
filename_05 = "Press-SwitchV0.5c-pc";

#-----------------------------------------------------------------------------
def showError(txt):
  print("Error: " + txt);

#-----------------------------------------------------------------------------
def md5(fname):
  hash_md5 = hashlib.md5()
  with open(fname, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
      hash_md5.update(chunk)
  return hash_md5.hexdigest()

#-----------------------------------------------------------------------------
def verifySingleFile(filename, desiredHash):
  print("Verifying " + filename + "...");
  if (not(os.path.exists(filename))):
    showError("File does not exist!");
    return False;

  actualHash = md5(filename);
  if (actualHash != desiredHash):
    showError("Checksum is not correct, please download the file again");
    print("Desired MD5: " + desiredHash);
    print("Actual MD5 : " + actualHash);
    return False;

  print("Succeeded");
  return True;

#-----------------------------------------------------------------------------
def unzipFile(filename):
  print("Unzipping file " + filename + "...");
  with zipfile.ZipFile(filename, 'r') as zip_ref:
    zip_ref.extractall(".")

#-----------------------------------------------------------------------------
def removeDir(filename):
  if (os.path.isdir(pathlib.Path(filename))):
    print("Removing directory " + filename + "...");
    shutil.rmtree(filename);

#-----------------------------------------------------------------------------
def checkFile(dirname, checksum):
  if (os.path.isdir(pathlib.Path(dirname))):
    print("Directory " + dirname + " exists, ZIP extract skipped");
    return True;

  filename = dirname + ".zip";
  if (not(verifySingleFile(filename, checksum))):
    return False;

  unzipFile(filename);
  return True;

#-----------------------------------------------------------------------------
def doMakeDir(path):
  if (os.path.isdir(pathlib.Path(path))):
    print("Directory " + path + " already exists, skipping creation");
  else:
    print("Creating directory " + path);
    os.mkdir(path);

#-----------------------------------------------------------------------------
def doCopyFile(srcPath, dstPath, filename):
  srcFile = os.path.join(srcPath, filename);
  print("Copying file " + srcFile + " into " + dstPath);
  shutil.copy(srcFile, dstPath);

#-----------------------------------------------------------------------------
# Main program
def main(argv):
  doClean = False;

  try:
    opts, args = getopt.getopt(argv, "", ["clean"])
  except getopt.GetoptError:
    showError('Usage is: press-stitch.py [--clean]');
    sys.exit(1);

  for opt, arg in opts:
    if (opt == "--clean"):
      doClean = True;

  if (doClean):
    removeDir(filename_03);
    removeDir(filename_04);
    removeDir(filename_05);
    removeDir("Extracted");
    sys.exit(0);

  # Normal run
  if (not(checkFile(filename_03, "e01bfc54520e8251bc73c7ee128836e2"))):
    sys.exit(1);

  if (not(checkFile(filename_04, "ca7ee44f40f802009a6d49659c8a760d"))):
    sys.exit(1);

  if (not(checkFile(filename_05, "6a4f9dac386e2fae1bce00e0157ee8b1"))):
    sys.exit(1);

  press_stitch_archive.extractAllRPAFiles();

  extPath4 = os.path.join("Extracted", filename_04);
  extPath5 = os.path.join("Extracted", filename_05);
  dstPath  = os.path.join(filename_05, "game");

  # Day-0.rpy
  print("Patching Day-0.rpy...");
  text_file = open(os.path.join(extPath5, "Story", "Day-0.rpy"), "r");
  lines = text_file.readlines();
  lines.insert(2848, (" " * 28) + "\"Maybe I was too quick to reject Eliza...\":\n");
  lines.insert(2849, (" " * 32) + "jump eliza\n");
  with open(os.path.join(dstPath, "Story", "Day-0.rpy"), "w") as outfile:
    outfile.writelines(lines);

  # Read ElizaPath.rpy into memory
  print("Patching ElizaPath.rpy...");
  text_file = open(os.path.join(extPath5, "Story", "ElizaPath.rpy"), "r");
  lines = text_file.readlines();

  # Do simple search-and-replace patching
  numLines = len(lines);
  i = 0;
  while i < numLines:
    lines[i] = lines[i].replace(" bg elizabedday",   " bg mansionelizaday");
    lines[i] = lines[i].replace(" bg elizabeddusk",  " bg mansionelizadusk");
    lines[i] = lines[i].replace(" bg elizabednight", " bg mansionelizalit");
    lines[i] = lines[i].replace(" bg mainbedday",    " bg mansioncalvinday");
    lines[i] = lines[i].replace(" bg mainbeddusk",   " bg mansioncalvindusk");
    i = i + 1;

  # Write the updated ElizaPath.rpy back out
  with open(os.path.join(dstPath, "Story", "ElizaPath.rpy"), "w") as outfile:
    outfile.writelines(lines);

  # Copy Eliza character graphics
  srcCharEliza = os.path.join(extPath4, "Characters", "Eliza");
  dstCharEliza = os.path.join(dstPath,  "Characters", "Eliza");
  doMakeDir(os.path.join(dstPath, "Characters"));
  doMakeDir(dstCharEliza);
  doCopyFile(srcCharEliza, dstCharEliza, "Eliza_Ex_017_003.png");
  doCopyFile(srcCharEliza, dstCharEliza, "Eliza_Ex_018_003.png");
  doCopyFile(srcCharEliza, dstCharEliza, "Eliza_Ex_019_003.png");
  doCopyFile(srcCharEliza, dstCharEliza, "Eliza_Ex_020_003.png");
  doCopyFile(srcCharEliza, dstCharEliza, "Eliza_Ex_021_003.png");
  doCopyFile(srcCharEliza, dstCharEliza, "Eliza_Ex_022_003.png");
  doCopyFile(srcCharEliza, dstCharEliza, "Eliza_Ex_Full_017_003.png");
  doCopyFile(srcCharEliza, dstCharEliza, "Eliza_Ex_Full_018_003.png");
  doCopyFile(srcCharEliza, dstCharEliza, "Eliza_Ex_Full_019_003.png");
  doCopyFile(srcCharEliza, dstCharEliza, "Eliza_Ex_Full_020_003.png");
  doCopyFile(srcCharEliza, dstCharEliza, "Eliza_Ex_Full_021_003.png");
  doCopyFile(srcCharEliza, dstCharEliza, "Eliza_Ex_Full_022_003.png");

  # Copy Michelle character graphics
  srcCharMichelle = os.path.join(extPath4, "Characters", "Michelle");
  dstCharMichelle = os.path.join(dstPath,  "Characters", "Michelle");
  doMakeDir(dstCharMichelle);
  doCopyFile(srcCharMichelle, dstCharMichelle, "Michelle_Ex_013_002.png");
  doCopyFile(srcCharMichelle, dstCharMichelle, "Michelle_Ex_014_002.png");
  doCopyFile(srcCharMichelle, dstCharMichelle, "Michelle_Ex_015_002.png");
  doCopyFile(srcCharMichelle, dstCharMichelle, "Michelle_Ex_015_Open_002.png");
  doCopyFile(srcCharMichelle, dstCharMichelle, "Michelle_Ex_016_002.png");
  doCopyFile(srcCharMichelle, dstCharMichelle, "Michelle_Ex_017_003.png");
  doCopyFile(srcCharMichelle, dstCharMichelle, "Michelle_Ex_018_003.png");
  doCopyFile(srcCharMichelle, dstCharMichelle, "Michelle_Ex_019_003.png");
  doCopyFile(srcCharMichelle, dstCharMichelle, "Michelle_Ex_020_003.png");
  doCopyFile(srcCharMichelle, dstCharMichelle, "Michelle_Ex_021_003.png");
  doCopyFile(srcCharMichelle, dstCharMichelle, "Michelle_Ex_Full_013_002.png");
  doCopyFile(srcCharMichelle, dstCharMichelle, "Michelle_Ex_Full_014_002.png");
  doCopyFile(srcCharMichelle, dstCharMichelle, "Michelle_Ex_Full_015_002.png");
  doCopyFile(srcCharMichelle, dstCharMichelle, "Michelle_Ex_Full_015_Open_002.png");
  doCopyFile(srcCharMichelle, dstCharMichelle, "Michelle_Ex_Full_016_002.png");
  doCopyFile(srcCharMichelle, dstCharMichelle, "Michelle_Ex_Full_017_003.png");
  doCopyFile(srcCharMichelle, dstCharMichelle, "Michelle_Ex_Full_018_003.png");
  doCopyFile(srcCharMichelle, dstCharMichelle, "Michelle_Ex_Full_019_003.png");
  doCopyFile(srcCharMichelle, dstCharMichelle, "Michelle_Ex_Full_020_003.png");
  doCopyFile(srcCharMichelle, dstCharMichelle, "Michelle_Ex_Full_021_003.png");

#-----------------------------------------------------------------------------
# Hook to call main
if __name__ == "__main__":
  main(sys.argv[1:])
