# -----------------------------------------------------------------------------
# press-stitch.py
# Merges the three Press Switch games together
# pylint: disable=bad-indentation
# -----------------------------------------------------------------------------

import getopt
import hashlib
import os.path
import pathlib
import shutil
import sys
import csv
import copy
import zipfile
import press_stitch_archive
import rpp

filename_03 = "Press-SwitchV0.3b-all"
filename_04 = "Press-SwitchV0.4a-pc"
filename_05 = "Press-SwitchV0.5c-pc"
filename_06 = "P-S-0.6a-pc"
filename_illia = "Illia's-MansionV1.0-pc"

# -----------------------------------------------------------------------------
def printRed(s):
    # type: (str) -> None
    print("\033[1;31m" + s + "\033[0m")

# -----------------------------------------------------------------------------
def showError(txt):
    # type: (str) -> None
    printRed("Error: " + txt)

# -----------------------------------------------------------------------------
def flagError(rpFile, lineNum, txt):
    # type: (rpp.RenPyFile, int, str) -> str
    showError("Line " + str(lineNum) + ": " + txt)
    if inlineErrors:
        return rpFile.lines[lineNum].strip('\n') + "  # ERROR: " + txt + "\n"

    sys.exit(1)

# -----------------------------------------------------------------------------
def md5(fname):
    # type: (str) -> str
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# -----------------------------------------------------------------------------
def verifySingleFile(filename, desiredHash):
    # type: (str, str) -> bool
    print("Verifying " + filename + "...")
    if (not(os.path.exists(filename))):
        showError("File does not exist!")
        return False

    actualHash = md5(filename)
    if (actualHash != desiredHash):
        showError("Checksum is not correct, please download the file again")
        print("Desired MD5: " + desiredHash)
        print("Actual MD5 : " + actualHash)
        return False

    print("Succeeded")
    return True

# -----------------------------------------------------------------------------
def unzipFile(filename):
    # type: (str) -> None
    print("Unzipping file " + filename + "...")
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(".")

# -----------------------------------------------------------------------------
def removeDir(filename):
    # type: (str) -> None
    if os.path.isdir(pathlib.Path(filename)):
        print("Removing directory " + filename + "...")
        shutil.rmtree(filename)

# -----------------------------------------------------------------------------
def checkFile(dirname, checksum):
    # type: (str, str) -> bool
    if os.path.isdir(pathlib.Path(dirname)):
        print("Directory " + dirname + " exists, ZIP extract skipped")
        return True

    filename = dirname + ".zip"
    if not(verifySingleFile(filename, checksum)):
        return False

    unzipFile(filename)
    return True

# -----------------------------------------------------------------------------
def doMakeDir(path):
    # type: (str) -> None
    if (os.path.isdir(pathlib.Path(path))):
        print("Directory " + path + " already exists, skipping creation")
    else:
        print("Creating directory " + path)
        os.mkdir(path)

# -----------------------------------------------------------------------------
def doCopyFile(srcPath, dstPath, filename):
    # type: (str, str, str) -> None
    srcFile = os.path.join(srcPath, filename)
    print("Copying file " + srcFile + " into " + dstPath)
    shutil.copy(srcFile, dstPath)

# -----------------------------------------------------------------------------
# Main program
def main(argv):
    doClean = False
    doEngine = False

    try:
        opts, args = getopt.getopt(argv, "", ["clean", "engine"])
    except getopt.GetoptError:
        showError('Usage is: extract.py [--clean]')
        sys.exit(1)

    for opt, arg in opts:
        if (opt == "--clean"):
            doClean = True
        elif (opt == "--engine"):
            doEngine = True

    if (doClean):
        removeDir(filename_03)
        removeDir(filename_04)
        removeDir(filename_05)
        removeDir(filename_06)
        removeDir("Extracted")
        sys.exit(0)

    have3 = False
    have4 = False
    have5 = False
    haveIllia = False
    if os.path.exists(filename_03 + ".zip"):
        if not(checkFile(filename_03, "e01bfc54520e8251bc73c7ee128836e2")):
            sys.exit(1)
        have3 = True
        press_stitch_archive.unpackArchive(filename_03)

    if os.path.exists(filename_04 + ".zip"):
        if not(checkFile(filename_04, "ca7ee44f40f802009a6d49659c8a760d")):
            sys.exit(1)
        have4 = True
        press_stitch_archive.unpackArchive(filename_04)

    if os.path.exists(filename_illia + ".zip"):
        if not(checkFile(filename_illia, "b5ae118b07ea2c37f46d8da27df749ae")):
            sys.exit(1)
        haveIllia = True
        press_stitch_archive.unpackArchive(filename_illia)

    if os.path.exists(filename_05 + ".zip"):
        if not(checkFile(filename_05, "6a4f9dac386e2fae1bce00e0157ee8b1")):
            sys.exit(1)
        have5 = True
        press_stitch_archive.unpackArchive(filename_05)

    if not(checkFile(filename_06, "8af387b938b2fcba32fd88848f042a32")):
        sys.exit(1)
    press_stitch_archive.unpackArchive(filename_06)

    patchBase = os.path.join("Patch", filename_06)
    patchPath = os.path.join(patchBase, "game")
    doMakeDir("Patch")
    doMakeDir(patchBase)
    doMakeDir(patchPath)

    if doEngine:
        shutil.copy(os.path.join("GameFiles", "body.py"), patchPath);
        shutil.copy(os.path.join("GameFiles", "body_data.py"), patchPath);
        shutil.copy(os.path.join("GameFiles", "screens.rpy"), patchPath);

    print("Done");

# -----------------------------------------------------------------------------
# Hook to call main
if __name__ == "__main__":
    main(sys.argv[1:])
