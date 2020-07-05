def appendText (filename : str):
    array = []
    with open(filename, "r") as f:
        array = f.read().splitlines()
    return array