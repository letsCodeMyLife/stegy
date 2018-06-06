class invalidFileTypeError(TypeError): pass


class cantCombine2JpgsError(Exception): pass


def isJpg(file):
    with open(file, "rb") as file:
        data = file.read()
        if data[:2] == b"\xFF\xD8" and data[-2:] == b"\xFF\xD9":
            return True
        else:
            return False

def encode(file1, file2, outFile):
    if isJpg(file1):
        with open(file1, "rb") as file:
            jpgData = file.read()

        with open(file2, "rb") as file:
            fileData = file.read()

        with open(outFile, "wb") as file:
            file.write(jpgData + fileData)
    elif isJpg(file2):
        with open(file2, "rb") as file:
            jpgData = file.read()

        with open(file1, "rb") as file:
            fileData = file.read()

        with open(outFile, "wb") as file:
            file.write(jpgData + fileData)
    elif isJpg(file1) and isJpg(file2):
        raise cantCombine2JpgsError("Cant combine two jpg files")
    else:
        raise invalidFileTypeError("One of the files must be an jpg file")
