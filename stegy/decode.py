import re


class cantDecodeError(Exception): pass


def decode(jpgFile, outFile):
    inFile = jpgFile
    fileData = list()
    found = False

    with open(inFile, "rb") as file:
        lines = file.readlines()

        for i in range(len(lines)):
            if not found:
                search = re.search(b"\xFF\xD9", lines[i])

                if not search == None:
                    fileData.append(lines[i][search.span()[-1]:])
                    found = True
            else:
                fileData.append(lines[i])

    if fileData == list():
        raise cantDecodeError("Cant decode file: {}".format(inFile))

    with open(outFile, "wb") as file:
        file.writelines(fileData)
