import pygame, math, sys, time
from Block import Block
from LevelChangeBlock import LevelChangeBlock
from Player import Player

class Level():
    def __init__(self, level, names, screenSize):
        self.screenSize = screenSize
        self.names = names
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.blocks = []
        self.hardBlocks = []
        self.levelChangeBlocks = []
        self.enemies = []
        self.players = []
        self.blockSize = 50
        self.level = level
        self.load(level)

        


    def load(self, level, source=None):
        while len(self.blocks) > 0:
            self.blocks.remove(self.blocks[0])
        while len(self.hardBlocks) > 0:
            self.hardBlocks.remove(self.hardBlocks[0])
        while len(self.levelChangeBlocks) > 0:
            self.levelChangeBlocks.remove(self.levelChangeBlocks[0])
        while len(self.enemies) > 0:
            self.enemies.remove(self.enemies[0])
        
            
        self.level = level
        print self.level
        geoMap="RSC/Maps/"+ level +".lvl"
        thingMap="RSC/Maps/"+ level +".tng"

        geofile = open(geoMap, "r")
        lines = geofile.readlines()
        geofile.close()
        newlines = []
        
        if source != None:
            if source.upper() == "N":
                plpos = [self.players[0].rect.center[0], self.screenHeight-75]
            elif source.upper() == "S":
                plpos = [self.players[0].rect.center[0], 75]
            elif source.upper() == "W":
                plpos = [self.screenWidth-75, self.players[0].rect.center[1]]
            elif source.upper() == "E":
                plpos = [75, self.players[0].rect.center[1]]
            self.players[0].place(plpos)
        

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
                    self.hardBlocks += [Block("RSC/Block/bush.png",
                                    [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                    (self.blockSize,self.blockSize))]
                    self.blocks += [self.hardBlocks[-1]]
                if c == "*":
                    self.blocks += [Block("RSC/Block/block.png",
                                    [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                    (self.blockSize,self.blockSize))]

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
                    if len(self.players) == 0:
                        if len(self.names) > 0:
                            daName = self.names.pop()
                            self.players += [Player(daName,  [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)])]
                if c == "N":
                    newlev = self.level[:7] + str(int(self.level[7])+1)
                    self.levelChangeBlocks += [LevelChangeBlock(
                                                                [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                                                (self.blockSize, self.blockSize),
                                                                newlev, c)]
                if c == "n":
                    newlev = self.level[:7] + str(int(self.level[7])+1)
                    self.levelChangeBlocks += [LevelChangeBlock(
                                                                [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                                                (self.blockSize,self.blockSize),
                                                                newlev, c)]
                if c == "S":
                    newlev = self.level[:7] + str(int(self.level[7])-1)
                    self.levelChangeBlocks += [LevelChangeBlock(
                                                                [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                                                (self.blockSize,self.blockSize),
                                                                newlev, c)]
                if c == "s":
                    newlev = self.level[:7] + str(int(self.level[7])-1)
                    self.levelChangeBlocks += [LevelChangeBlock(
                                                                [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                                                (self.blockSize,self.blockSize),
                                                                newlev, c)]
                if c == "W":
                    newlev = self.level[:6] + str(int(self.level[6])-1) + self.level[7]
                    self.levelChangeBlocks += [LevelChangeBlock(
                                                                [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                                                (self.blockSize,self.blockSize),
                                                                newlev, c)]
                if c == "w":
                    newlev = self.level[:6] + str(int(self.level[6])-1) + self.level[7]
                    self.levelChangeBlocks += [LevelChangeBlock(
                                                                [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                                                (self.blockSize,self.blockSize),
                                                                newlev, c)]
                if c == "E":
                    newlev = self.level[:6] + str(int(self.level[6])+1) + self.level[7]
                    self.levelChangeBlocks += [LevelChangeBlock(
                                                                [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                                                (self.blockSize,self.blockSize),
                                                                newlev, c)]
                if c == "e":
                    newlev = self.level[:6] + str(int(self.level[6])+1) + self.level[7]
                    self.levelChangeBlocks += [LevelChangeBlock(
                                                                [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                                                (self.blockSize,self.blockSize),
                                                                newlev, c)]
