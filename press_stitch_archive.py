import os.path
import subprocess
import sys
import rpatool

folderExtracted = "Extracted"
folderName = "Press-SwitchV0"
folderVersion = ['.3b-all', '.4a-pc', '.5c-pc']
fileNameArchive = "archive.rpa"
fileNameScripts = "scripts.rpa"
cwd = os.getcwd()

def extractRPAFile(rpaFilename, output):
    print("Extracting RPA file " + rpaFilename + " to " + output)

    try:
        archive = rpatool.RenPyArchive(rpaFilename)
    except IOError as e:
        print('Could not open archive file {0} for reading: {1}'.format(archive, e), file=sys.stderr)
        sys.exit(1)

    files = archive.list()

    # Create output directory if not present.
    if not os.path.exists(output):
        os.makedirs(output)

    # Iterate over files to extract.
    for filename in files:
        if filename.find('=') != -1:
            (outfile, filename) = filename.split('=', 2)
        else:
            outfile = filename

        try:
            contents = archive.read(filename)

            # Create output directory for file if not present.
            if not os.path.exists(os.path.dirname(os.path.join(output, outfile))):
                os.makedirs(os.path.dirname(os.path.join(output, outfile)))

            with open(os.path.join(output, outfile), 'wb') as file:
                file.write(contents)
        except Exception as e:
            print('Could not extract file {0} from archive: {1}'.format(filename, e), file=sys.stderr)

#Unpackages scripts and archive rpas using rpatool. These go from the Press-SwitchV0x folder to extracted\Press-SwitchV0x
def unpackArchive(folder):
    folderArchive = (os.path.join(cwd , folderName + folder , "game", ""))
    print("Processing " + folder + " This might take a hot minute...")
    destinationFolder = os.path.join(folderExtracted , folderName + folder)
    extractRPAFile(folderArchive + fileNameArchive, destinationFolder)
    if (not(folder == ".3b-all")):
        extractRPAFile(folderArchive + fileNameScripts, destinationFolder)

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

#Extract all the RPA files. Called both by main and by the press-stitch.py script.
def extractAllRPAFiles():
    if (not(os.path.exists(folderExtracted))):
        os.mkdir(folderExtracted)
    for ver in folderVersion:
        extractFolder = os.path.join(folderExtracted, folderName + ver)
        if (not(os.path.exists(extractFolder))):
            createFolders(ver)
            verifyFolders(ver)
            unpackArchive(ver)
        else:
            print("Extracted data folder " + extractFolder + " exists, skipping RPA extract");

#It's main yay. Calls above functions.
def main(argv):
    extractAllRPAFiles()

if __name__ == "__main__":
    main(sys.argv[1:])
