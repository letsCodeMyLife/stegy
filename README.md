# stegy
Steganography

This library can hide other files in jpg files.

Example:

    import stegy
    stegy.encode("jpgfile.jpg", "zipfile.zip", "hidden.jpg")
    stegy.decode("hidden.jpg", "extractedzip.zip")
