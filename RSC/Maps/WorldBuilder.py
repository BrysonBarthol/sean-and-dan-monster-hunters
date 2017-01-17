import os

files = os.listdir("./")

newFiles = []
for f in files:
    if f[-4:] == ".tng":
        newFiles += [f]

files = newFiles
print files
