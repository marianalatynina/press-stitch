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

  # Day-0.rpy
  print("Patching Day-0.rpy...");
  text_file = open(os.path.join("Extracted", filename_05, "Story", "Day-0.rpy"), "r");
  lines = text_file.readlines();
  lines.insert(2848, (" " * 28) + "\"Maybe I was too quick to reject Eliza...\":\n");
  lines.insert(2849, (" " * 32) + "jump eliza\n");
  with open(os.path.join(filename_05, "game", "Story", "Day-0.rpy"), "w") as outfile:
    outfile.writelines(lines);

#-----------------------------------------------------------------------------
# Hook to call main
if __name__ == "__main__":
  main(sys.argv[1:])
