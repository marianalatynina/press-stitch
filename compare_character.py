#-----------------------------------------------------------------------------
# compare_character.py
# Checks an extracted character's graphics to see what's changed between
# version 0.3 and 0.5
#-----------------------------------------------------------------------------

import getopt
import hashlib
import os.path
import pathlib
import shutil
import subprocess
import sys
import zipfile

filename_03 = "Press-SwitchV0.3b-all";
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
def doCrop(srcDir):
  dstDir = srcDir + "Cropped";
  doMakeDir(dstDir);
  for pic in os.listdir(srcDir):
    if pic.endswith(".png"):
      srcFile = os.path.join(srcDir, pic);
      dstFile = os.path.join(dstDir, pic + ".pnm");
      print("Cropping " + srcFile);
      cmd = ["convert", "-size", "1024x1024", "xc:#ffffffff", srcFile,
             "-compose", "Over", "-composite", "-trim", dstFile];
      cmd_result = subprocess.run(cmd);
      if (cmd_result.returncode != 0):
        showError("Imagemagick convert returned " + str(cmd_result.returncode));
        sys.exit(1);

#-----------------------------------------------------------------------------
def buildIndex(path):
  idx = {};
  for pic in os.listdir(path):
    if pic.endswith(".pnm"):
      idx[md5(os.path.join(path, pic))] = pic;

  return idx;

#-----------------------------------------------------------------------------
def leftAlign(s, ln):
  return s + (" " * (ln - len(s)));

#-----------------------------------------------------------------------------
def printArrayEntry(src, dst, comment):
  first  = leftAlign("\"" + src.split(".")[0].lower() + "\":", 40);
  second = leftAlign("\"" + dst.split(".")[0].lower() + "\",", 40);
  print("  " + first + " " + second + " # Auto: " + comment);

#-----------------------------------------------------------------------------
def insertNumber(filename, numToInsert):
  fields = filename.split('.');
  return(fields[0] + numToInsert + "." + fields[1] + "." + fields[2]);

#-----------------------------------------------------------------------------
# Main program
def main(argv):
  if (len(argv) < 1):
    showError("Usage is: compare_character.py <character name>");
    sys.exit(1)

  asArray = False;
  if (len(argv) > 1) and (argv[1] == "--code"):
    asArray = True;

  characterName = argv[0];
  srcDir3 = os.path.join("Extracted", filename_03, "Character images", characterName);
  srcDir5 = os.path.join("Extracted", filename_05, "Characters", characterName);

  # Sanity check
  if (not(os.path.isdir(pathlib.Path(srcDir3)))):
    showError("Character " + characterName + " not found in 0.3 Graphics directory");
    sys.exit(1);
  if (not(os.path.isdir(pathlib.Path(srcDir5)))):
    showError("Character " + characterName + " not found in 0.5 Graphics directory");
    sys.exit(1);

  srcDir3Crop = srcDir3 + "Cropped";
  srcDir5Crop = srcDir5 + "Cropped";

  # Do we need to crop images for 0.3?
  if (not(os.path.isdir(pathlib.Path(srcDir3Crop)))):
    doCrop(srcDir3);

  # Do we need to crop images for 0.5?
  if (not(os.path.isdir(pathlib.Path(srcDir5Crop)))):
    doCrop(srcDir5);

  # Build an index of the MD5 hashes for 0.5
  idx = buildIndex(srcDir5Crop);

  # Sort the list of files in 0.3
  fileList = os.listdir(srcDir3Crop);
  fileList.sort();

  if asArray:
    print("characterMap" + characterName + " = {");

  # Iterate 0.3
  fileWidth = 40;
  for pic in fileList:
    if pic.endswith(".pnm"):
      chksum = md5(os.path.join(srcDir3Crop, pic));
      file1 = insertNumber(pic, "_001");
      file2 = insertNumber(pic, "_002");
      file3 = insertNumber(pic, "_003");

      if asArray:
        if (chksum in idx):
          filename5 = idx.get(chksum);
          if filename5 == pic:
            # Same
            printArrayEntry(pic, pic, "Same");
          else:
            # Renamed
            printArrayEntry(pic, filename5, "Renamed");
        else:
          if os.path.exists(os.path.join(srcDir5Crop, pic)):
            # Edited
            printArrayEntry(pic, pic, "Edited");
          elif os.path.exists(os.path.join(srcDir5Crop, file1)):
            # Edited and renamed
            printArrayEntry(pic, file1, "Edited and renamed");
          elif os.path.exists(os.path.join(srcDir5Crop, file2)):
            # Edited and renamed
            printArrayEntry(pic, file2, "Edited and renamed");
          elif os.path.exists(os.path.join(srcDir5Crop, file3)):
            # Edited and renamed
            printArrayEntry(pic, file3, "Edited and renamed");
          else:
            # Deleted
            printArrayEntry(pic, "", "Deleted");
      else:
        if chksum in idx:
          filename5 = idx.get(chksum);
          if filename5 == pic:
            print(leftAlign(pic, fileWidth) + ": Same");
          else:
            printGreen(leftAlign(pic, fileWidth) + ": Renamed to " + filename5);
        else:
          if os.path.exists(os.path.join(srcDir5Crop, pic)):
            printYellow(leftAlign(pic, fileWidth) + ": Edited");
          else:
            printRed(leftAlign(pic, fileWidth) + ": Deleted");

  if asArray:
    print("}");

#-----------------------------------------------------------------------------
# Hook to call main
if __name__ == "__main__":
  main(sys.argv[1:])
