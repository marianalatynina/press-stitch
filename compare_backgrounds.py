#-----------------------------------------------------------------------------
# compare_backgrounds.py
# Checks an extracted background's graphics to see what's changed between
# version 0.4 and 0.5
#-----------------------------------------------------------------------------

import getopt
import hashlib
import os.path
import pathlib
import shutil
import subprocess
import sys
import zipfile

filename_04 = "Press-SwitchV0.4a-pc";
filename_05 = "Press-SwitchV0.5c-pc";


#-----------------------------------------------------------------------------
def printGreen(s):
  print("\033[1;32m" + s + "\033[0m");

#-----------------------------------------------------------------------------
def printRed(s):
  print("\033[1;31m" + s + "\033[0m");

#-----------------------------------------------------------------------------
def printYellow(s):
  print("\033[1;33m" + s + "\033[0m");

#-----------------------------------------------------------------------------
def showError(txt):
  printRed("Error: " + txt);

#-----------------------------------------------------------------------------
def md5(fname):
  hash_md5 = hashlib.md5()
  with open(fname, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
      hash_md5.update(chunk)
  return hash_md5.hexdigest()

#-----------------------------------------------------------------------------
def doMakeDir(path):
  if (os.path.isdir(pathlib.Path(path))):
    print("Directory " + path + " already exists, skipping creation");
  else:
    print("Creating directory " + path);
    os.mkdir(path);

#-----------------------------------------------------------------------------
def buildIndex(path):
  idx = {};
  for pic in os.listdir(path):
    if pic.endswith(".jpg"):
      idx[md5(os.path.join(path, pic))] = pic;

  return idx;

#-----------------------------------------------------------------------------
def leftAlign(s, ln):
  return s + (" " * (ln - len(s)));

#-----------------------------------------------------------------------------
def printArrayEntry(src, dst, comment):
  first  = leftAlign("\"" + src.split(".")[0].lower().replace('_', '')  + "\":", 30);
  second = leftAlign("\"" + dst.split(".")[0].lower().replace('_', '')  + "\",", 30);
  print("  " + first + " " + second + " # Auto: " + comment);

#-----------------------------------------------------------------------------
# Main program
def main(argv):
  srcDir4 = os.path.join("Extracted", filename_04, "Backgrounds");
  srcDir5 = os.path.join("Extracted", filename_05, "Backgrounds");

  # Sanity check
  if (not(os.path.isdir(pathlib.Path(srcDir4)))):
    showError("Directory " + srcDir4 + " not found");
    sys.exit(1);
  if (not(os.path.isdir(pathlib.Path(srcDir5)))):
    showError("Directory " + srcDir5 + " not found");
    sys.exit(1);

  # Build an index of the MD5 hashes for 0.5
  idx = buildIndex(srcDir5);

  # Sort the list of files in 0.4
  fileList = os.listdir(srcDir4);
  fileList.sort();

  print("backgroundMap = {");

  # Iterate 0.4
  fileWidth = 40;
  for pic in fileList:
    if pic.endswith(".jpg"):
      chksum = md5(os.path.join(srcDir4, pic));

      if (chksum in idx):
        filename5 = idx.get(chksum);
        if filename5 == pic:
          # Same
          printArrayEntry(pic, pic, "Same");
        else:
          # Renamed
          printArrayEntry(pic, filename5, "Renamed");
      else:
        if os.path.exists(os.path.join(srcDir5, pic)):
          # Edited
          printArrayEntry(pic, pic, "Edited");
        else:
          # Deleted
          printArrayEntry(pic, "", "Deleted");

  print("};");

#-----------------------------------------------------------------------------
# Hook to call main
if __name__ == "__main__":
  main(sys.argv[1:])
