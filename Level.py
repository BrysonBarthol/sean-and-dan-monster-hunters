import pygame, math, sys, time
from Block import Block

class Level():
    def __init__(self, level, screenSize):
        self.screenSize = screenSize
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.blocks = []
        self.enemies = []
        self.player
        self.load(level)
        self.blockSize = 50
        
        
    def load(self, level):
        geoMap="RCS/Maps/"+ level +".lvl"
        thingMap="RCS/Maps/"+ level +".tng"

        geofile = open(geoMap, "r")
        lines = geofile.readlines()
        geofile.close()
        newlines = []
		
		#Clean up the file by stripping newlines!
        for line in lines:
            newline = ""
            for character in line:
                if character != "\n":
                    newline += character
            newlines += [newline]
            
        for y, line in enumerate(newlines):
            for x, c in enumerate(line):
                if c == "#":
                    self.blocks += [Block([(x*10)+5, (y*10)+5], 
                                           self.screenSize,
                                           "rcs/imgs/block/cobblestone.png",
                                           (10,10)
                                           )]
#-------Blocks
                
                    
        #----Done with file---
        
        thingfile = open(thingMap, "r")
        lines = thingfile.readlines()
        thingfile.close() 
        
        newlines = []
        
        for line in lines:
            newline = ""
            for character in line:
                if character != "\n":
                    newline += character
            newlines += [newline]
            
        for y, line in enumerate(newlines):
            for x, c in enumerate(line):
#-------Blocks
                if c == "@":
                    self.darkblocks += [Block([(x*10)+5, (y*10)+5], 
                                            self.screenSize,
                                            "rcs/imgs/block/spawnspace.png",
                                            (10,10)
                                            )]
#-------Blocks
#-------Blocks

    
#-------Blocks
