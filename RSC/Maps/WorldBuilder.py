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



    print maxX, maxY



 
    wMap = [[]]

    for x in range(maxX):
        wMap[0] += [str(x+1)*20] + ['|']
    


    for y in range(maxY):
        line = [str(y+1)]
        for x in range(maxX):
            line += [" "*20] + ['|']
            print line
        for i in range(15):
            wMap += [line]
            print len(wMap), len(wMap[-1])
        wMap += ["-" * 21 * maxX + "-"]
        
        
    
 
    out = ""
    for l in wMap:
        for s in l:
            out += s
        out += '\n'
        

    outFile = open("wMap" + str(w+1) + ".txt", 'w')
    outFile.write(out)
    outFile.close()

