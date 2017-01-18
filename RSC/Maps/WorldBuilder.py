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
    

for w, world in enumerate(worlds):
    maxX = 0
    maxY = 0

    for f in world:
        if int(f[7]) > maxX:
            maxX = int(f[7])
        if int(f[8]) > maxY:
            maxY= int(f[8])

    #print maxX, maxY
    wMap = [[" "]]

    for x in range(maxX):
        wMap[0] += [str(x+1)*20] + ['|']
    
    for y in range(maxY):
        line = [str(y+1)]
        for x in range(maxX):
            line += [" "*20] + ['|']
        for i in range(15):
            wMap += [line]
        wMap += ["-" * 21 * maxX + "-"]
        
    for theWorld in world:
        f = open(theWorld, 'r')
        lines = f.readlines()
        f.close()
        
        thisX = (int(theWorld[7])-1) * 2 + 1
        thisY = (int(theWorld[8])-1) * 16 + 1
        
        print theWorld
        print thisX, thisY
        for al, theline in enumerate(lines):
            wMap[thisY+al][thisX] = theline[:-1]
            
        print wMap
    
    print wMap




    out = ""
    for l in wMap:
        for s in l:
            #print s
            out += s
        out += '\n'
        
    print out

    outFile = open("wMap" + str(w+1) + ".txt", 'w')
    outFile.write(out)
    outFile.close()

