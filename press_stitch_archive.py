import os.path
import sys

import rpatool

folderExtracted = "Extracted"
folderName = "Press-SwitchV0"
# folderVersion = ['.3b-all', '.4a-pc', '.5c-pc']
folderVersion = [".5c-pc"]
fileNameArchive = "archive.rpa"
fileNameScripts = "scripts.rpa"
cwd = os.getcwd()


def extractRPAFile(rpaFilename, output):
    # type: (str, str) -> None
    print(f"Extracting RPA file {rpaFilename} to {output}")

    try:
        archive = rpatool.RenPyArchive(rpaFilename)
    except IOError as e:
        print(
            "Could not open archive file {0} for reading: {1}".format(archive, e),
            file=sys.stderr,
        )
        sys.exit(1)

    files = archive.list()

    # Create output directory if not present.
    if not os.path.exists(output):
        os.makedirs(output)

    # Iterate over files to extract.
    for filename in files:
        if filename.find("=") != -1:
            (outfile, filename) = filename.split("=", 2)
        else:
            outfile = filename

        try:
            contents = archive.read(filename)

            # Create output directory for file if not present.
            if not os.path.exists(os.path.dirname(os.path.join(output, outfile))):
                os.makedirs(os.path.dirname(os.path.join(output, outfile)))

            with open(os.path.join(output, outfile), "wb") as file:
                file.write(contents)
        except Exception as e:
            print(
                "Could not extract file {0} from archive: {1}".format(filename, e),
                file=sys.stderr,
            )


# Unpackages scripts and archive rpas using rpatool. These go from the Press-SwitchV0x folder to extracted\Press-SwitchV0x
def unpackArchive(folder):
    # type: (str) -> None
    folderArchive = os.path.join(cwd, folder, "game", "")
    destinationFolder = os.path.join(folderExtracted, folder)
    if os.path.exists(destinationFolder):
        print(
            "Extracted data folder "
            + destinationFolder
            + " exists, skipping RPA extract"
        )
        return
    print(f"Extracting {folder}, please wait...")
    extractRPAFile(folderArchive + fileNameArchive, destinationFolder)
    if folder != f"{folderName}.3b-all":
        extractRPAFile(folderArchive + fileNameScripts, destinationFolder)


# Creates the folders to extract to
def createFolders(folder):
    # type: (str) -> None
    if not (os.path.exists(os.path.join(folderExtracted, folderName + folder))):
        os.mkdir(os.path.join(folderExtracted, folderName + folder))


# Verifies that source folders exist
def verifyFolders(folder):
    # type: (str) -> None
    if not (os.path.exists(folderName + folder)):
        print(folderName + folder)
        print("Data folders not present aborting")
        exit()


# Extract all the RPA files. Called both by main and by the press-stitch.py script.
def extractAllRPAFiles():
    # type: () -> None
    if not (os.path.exists(folderExtracted)):
        os.mkdir(folderExtracted)
    for ver in folderVersion:
        extractFolder = os.path.join(folderExtracted, folderName + ver)
        if not (os.path.exists(extractFolder)):
            createFolders(ver)
            verifyFolders(ver)
            unpackArchive(folderName + ver)
        else:
            print(
                "Extracted data folder "
                + extractFolder
                + " exists, skipping RPA extract"
            )


# It's main yay. Calls above functions.
def main(argv):
    # type: (list[str]) -> None
    extractAllRPAFiles()


if __name__ == "__main__":
    main(sys.argv[1:])
