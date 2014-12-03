import pygame, math, sys, time
from Block import Block

class Level():
    def __init__(self, level, screenSize):
        self.screenSize = screenSize
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.blocks = []
        self.levelChangeBlocks = []
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
                    self.blocks += [Block([(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)], 
                                           self.screenSize,
                                           "rcs/imgs/block/block.png",
                                           (self.blockSize,self.blockSize)
                                           )]
        for y, line in enumerate(newlines):
            for x, c in enumerate(line):
                if c == "#":
                    self.blocks += [Block([(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)], 
                                           self.screenSize,
                                           "rcs/imgs/block/block.png",
                                           (self.blockSize,self.blockSize)
                                           )]
        for y, line in enumerate(newlines):
            for x, c in enumerate(line):
                if c == "#":
                    self.blocks += [Block([(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)], 
                                           self.screenSize,
                                           "rcs/imgs/block/block.png",
                                           (self.blockSize,self.blockSize)
                                           )]
        for y, line in enumerate(newlines):
            for x, c in enumerate(line):
                if c == "#":
                    self.blocks += [Block([(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)], 
                                           self.screenSize,
                                           "rcs/imgs/block/block.png",
                                           (self.blockSize,self.blockSize)
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
                if c == "N":
					newlev = self.level[:7] + str(int(self.level[7]+1))
					self.levelChangeBlocks += [LevelChangeBlock(newlev,
					                                            (x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2) 
					                                            (self.blockSize,self.blockSize))]
				if c == "W":
					newlev = self.level[:6] + str(int(self.level[6]+1)+ self.level[7])
					self.levelChangeBlocks += [LevelChangeBlock(newlev,
					                                            (x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2) 
					                                            (self.blockSize,self.blockSize))]
