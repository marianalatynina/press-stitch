#-----------------------------------------------------------------------------
# compare_character.py
# Checks an extracted character's graphics to see what's changed between
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
      dstFile = os.path.join(dstDir, pic);
      print("Cropping " + srcFile);
      cmd = ["convert", "-size", "1024x1024", "xc:#ffffffff", srcFile,
             "-compose", "Over", "-composite", "-trim", dstFile];
      cmd_result = subprocess.run(cmd);
      if (cmd_result.returncode != 0):
        showError("Imagemagick convert returned " + str(cmd_result.returncode));
        sys.exit(1);

#-----------------------------------------------------------------------------
# Main program
def main(argv):
  if (len(argv) < 1):
    showError("Usage is: compare_character.py <character name>");
    sys.exit(1)

  characterName = argv[0];
  srcDir4 = os.path.join("Extracted", filename_04, "Characters", characterName);
  srcDir5 = os.path.join("Extracted", filename_05, "Characters", characterName);

  # Sanity check
  if (not(os.path.isdir(pathlib.Path(srcDir4)))):
    showError("Character " + characterName + " not found in 0.4 Graphics directory");
    sys.exit(1);
  if (not(os.path.isdir(pathlib.Path(srcDir5)))):
    showError("Character " + characterName + " not found in 0.5 Graphics directory");
    sys.exit(1);

  # Do we need to crop images for 0.4?
  if (not(os.path.isdir(pathlib.Path(srcDir4 + "Cropped")))):
    doCrop(srcDir4);

  # Do we need to crop images for 0.5?
  if (not(os.path.isdir(pathlib.Path(srcDir5 + "Cropped")))):
    doCrop(srcDir5);

#-----------------------------------------------------------------------------
# Hook to call main
if __name__ == "__main__":
  main(sys.argv[1:])
