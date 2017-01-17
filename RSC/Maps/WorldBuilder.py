import os

files = os.listdir("./")

worlds = [[],[],[]]
for f in files:
    if f[-4:] == ".tng":
        if f[6] == "1":
            worlds[0] += [f]
        elif f[6] == "2":
            worlds[1] += [f]
        elif f[6] == "3":
            worlds[2] += [f]

for world in worlds:
    for f in world:
        print f
    print "----------"
    

for world in worlds:
    maxX = 0
    maxY = 0

    for f in world:
        if int(f[7]) > maxX:
            maxX = int(f[7])
        if int(f[8]) > maxY:
            maxY= int(f[8])



    print maxX, maxY


""""
 
wMap1 = " "

for x in range(maxX1):
    wMap1 += str(x+1)*20 + '|'
    
wMap1 += "\n"

for y in range(maxY1):
    line = str(y+1)
    for x in range(maxX1):
        line += " "*20 + '|'
    line += '\n'
    wMap1 += line * 15 
    wMap1 += "-" * 21 * maxX1 + "-" + '\n'
    
outFile = open("wMap1.txt", 'w')
outFile.write(wMap1)
outFile.close()
"""
