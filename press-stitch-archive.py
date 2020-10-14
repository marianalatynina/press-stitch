import os.path
import glob
import sys

folderExtracted = "Extracted"
folderName = "Press-SwitchV0"
folderVersion = ['.3b-all', '.4a-pc', '.5c-pc']
fileNameArchive = "archive.rpa"
fileNameScripts = "scirpts.rpa"

def unpackArchive():
    pass

def createFolders(folder):
    if (not(os.path.exists(folderExtracted + "\\" + folderName + folder))):
        os.mkdir(folderExtracted + "\\" + folderName + folder)
    
def verifyFolders(folder):
    if (not(os.path.exists(folderExtracted + "\\" + folderName + folder))):
        print("Data folders not present aborting")
        return False
         
def main(argv):
    if (not(os.path.exists(folderExtracted))):
        os.mkdir(folderExtracted)
    
    for ver in folderVersion:
        createFolders(ver)
        verifyFolders(ver)

if __name__ == "__main__":
    main(sys.argv[1:])