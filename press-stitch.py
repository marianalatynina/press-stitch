import sys
import hashlib
import os.path

filename_03 = "Press-SwitchV0.3b-all.zip";
filename_04 = "Press-SwitchV0.4a-pc.zip";
filename_05 = "Press-SwitchV0.5c-pc.zip";

def showError(txt):
  print("Error: " + txt);

def md5(fname):
  hash_md5 = hashlib.md5()
  with open(fname, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
      hash_md5.update(chunk)
  return hash_md5.hexdigest()

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

def verifyZIPFiles():
  if (not(verifySingleFile(filename_03, "e01bfc54520e8251bc73c7ee128836e2"))):
    return False;

  if (not(verifySingleFile(filename_04, "ca7ee44f40f802009a6d49659c8a760d"))):
    return False;

  if (not(verifySingleFile(filename_05, "6a4f9dac386e2fae1bce00e0157ee8b1"))):
    return False;

  return True;

verifyZIPFiles();

