import os.path
import subprocess
import sys

folderExtracted = "Extracted"
folderName = "Press-SwitchV0"
folderVersion = ['.3b-all', '.4a-pc', '.5c-pc']
fileNameArchive = "archive.rpa"
fileNameScripts = "scripts.rpa"
cwd = os.getcwd()

#Unpackages scripts and archive rpas using rpatool. These go from the Press-SwitchV0x folder to extracted\Press-SwitchV0x
def unpackArchive(folder):
    folderArchive = (os.path.join(cwd , folderName + folder , "game", ""))
    print("Processing " + folder + " This might take a hot minute...")
    destinationFolder = os.path.join(folderExtracted , folderName + folder)
    executable = os.path.join(cwd, "rpatool")
    command = executable + " -x " + (folderArchive + "archive.rpa -o " + destinationFolder)
    print("Running command: " + command)
    subprocess.run(command, shell=True)

#Creates the folders to extract to
def createFolders(folder):
    if (not(os.path.exists(os.path.join(folderExtracted , folderName + folder)))):
        os.mkdir(os.path.join(folderExtracted , folderName + folder))

#Verifies that source folders exist
def verifyFolders(folder):
    if (not(os.path.exists(folderName + folder))):
        print (folderName + folder)
        print("Data folders not present aborting")
        exit()

#It's main yay. Calls above functions.
def main(argv):
    if (not(os.path.exists(folderExtracted))):
        os.mkdir(folderExtracted)
    for ver in folderVersion:
        createFolders(ver)
        verifyFolders(ver)
        unpackArchive(ver)
    exit()

if __name__ == "__main__":
    main(sys.argv[1:])
