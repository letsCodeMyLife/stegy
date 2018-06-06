# stegy
Steganography

This library can hide other files in jpg files.

Example:

    import stegy
    stegy.encode.encode("jpgfile.jpg", "zipfile.zip", "hided.jpg")
    stegy.decode.decode("hided.jpg", "extractedzip.zip")
