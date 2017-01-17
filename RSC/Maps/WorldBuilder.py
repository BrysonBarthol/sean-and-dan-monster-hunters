import os

files = os.listdir("./")

w1 = []
w2 = []
w3 = []
for f in files:
    if f[-4:] == ".tng":
        if f[6] == "1":
            w1 += [f]
        elif f[6] == "2":
            w2 += [f]
        elif f[6] == "3":
            w3 += [f]

files = newFiles
print files
