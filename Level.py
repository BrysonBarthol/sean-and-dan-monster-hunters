import pygame, math, sys, time, os
from Block import Block
from LevelChangeBlock import LevelChangeBlock
from Door import Door
from Player import Player
from Ghost import Ghost
from Demon import Demon
from Leviathan import Leviathan
from Pestilence import Pestilence
from War import War
from Death import Death
from Pot import Pot
from Key import Key

class Level():
    def __init__(self, level, names, screenSize):
        self.screenSize = screenSize
        self.names = names
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.blocks = []
        self.keys = []
        self.hardBlocks = []
        self.portals = []
        
        self.levelChangeBlocks = []
        self.doors = []
        self.ghosts = []
        self.leviathans = []
        self.demons = []
        self.pestilences = []
        self.wars = []
        self.deaths = []
        self.pots = [] 
        self.pot = [] 
        
        
        self.players = []
        
        self.blockSize = 50
        self.level = level
        self.load(level)
        

    def killOldLevels(self, timeInSeconds):
        for f in os.listdir("RSC/Maps/"):
            if f[-5:] == ".tngs":
                print f, time.time() - os.path.getmtime("RSC/Maps/"+f), timeInSeconds
                if (time.time() - os.path.getmtime("RSC/Maps/"+f)) > timeInSeconds:
                    print f
                    os.remove("RSC/Maps/"+f)
            
    
    def unload(self):
        things = []
        line = []
        for y in range(14):
            for x in range(20):
                line += [" "]
            things += [line]
            line = []
        #print len(things), len(things[0])
        
        for ghost in self.ghosts:
            things[ghost.rect.center[1]/50][ghost.rect.center[0]/50] = "G"
        for leviathan in self.leviathans:
            things[leviathan.rect.center[1]/50][leviathan.rect.center[0]/50] = "L"
        for demon in self.demons:
            things[demon.rect.center[1]/50][demon.rect.center[0]/50] = "D"
        for pestilence in self.pestilences:
            things[pestilence.rect.center[1]/50][pestilence.rect.center[0]/50] = "!"
        for war in self.wars:
            things[war.rect.center[1]/50][war.rect.center[0]/50] = "A"
        for pot in self.pots:
            things[pot.rect.center[1]/50][pot.rect.center[0]/50] = "T"
        for lc in self.levelChangeBlocks:
            things[lc.rect.center[1]/50][lc.rect.center[0]/50] = lc.kind
        for lc in self.doors:
            things[lc.rect.center[1]/50][lc.rect.center[0]/50] = lc.kind
        for lc in self.portals:
            things[lc.rect.center[1]/50][lc.rect.center[0]/50] = lc.kind
        
        thingString = ""
        for line in things:
            for c in line:
                thingString += c
            thingString += "\n"
        #print thingString
        
        thingMap="RSC/Maps/"+ self.level +".tngs"
        savedThingfile = open(thingMap, "w")
        savedThingfile.write(thingString)
        savedThingfile.close()
            
        while len(self.blocks) > 0:
            self.blocks.remove(self.blocks[0])
        while len(self.keys) > 0:
            self.keys.remove(self.keys[0])
        while len(self.portals) > 0:
            self.portals.remove(self.portals[0])
        while len(self.hardBlocks) > 0:
            self.hardBlocks.remove(self.hardBlocks[0])
        while len(self.levelChangeBlocks) > 0:
            self.levelChangeBlocks.remove(self.levelChangeBlocks[0])
        while len(self.doors) > 0:
            self.doors.remove(self.doors[0])
        while len(self.ghosts) > 0:
            self.ghosts.remove(self.ghosts[0])
        while len(self.demons) > 0:
            self.demons.remove(self.demons[0])
        while len(self.leviathans) > 0:
            self.leviathans.remove(self.leviathans[0])
        while len(self.pestilences) > 0:
            self.pestilences.remove(self.pestilences[0])
        while len(self.wars) > 0:
            self.wars.remove(self.wars[0])
        while len(self.deaths) > 0:
            self.deaths.remove(self.deaths[0])
        while len(self.pots) > 0:
            self.pots.remove(self.pots[0])
    
    def load(self, level, source=None):  
        if source != None:
            self.unload()    
        self.killOldLevels(30)
        self.level = level
        print self.level
        geoMap="RSC/Maps/"+ level +".lvl"
        thingMap="RSC/Maps/"+ level +".tng"
        savedThingMap="RSC/Maps/"+ level +".tngs"

        geofile = open(geoMap, "r")
        lines = geofile.readlines()
        geofile.close()
        newlines = []
        
        if source != None:
            if source.upper() != "O":
                if source.upper() == "N":
                    plpos = [self.players[0].rect.center[0], self.screenHeight-75]
                elif source.upper() == "S":
                    plpos = [self.players[0].rect.center[0], 75]
                elif source.upper() == "W":
                    plpos = [self.screenWidth-75, self.players[0].rect.center[1]]
                elif source.upper() == "E":
                    plpos = [75, self.players[0].rect.center[1]]
                elif source.upper() == "2":
                    plpos = [self.players[0].rect.center[0], 75]
                elif source.upper() == "3":
                    plpos = [75, self.players[0].rect.center[1]]
                elif source.upper() == "7":
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
                    world = int(self.level[6])
                    if world == 1:
                        self.hardBlocks += [Block("RSC/Block/bush.png",
                                        [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                        (self.blockSize,self.blockSize))]
                    elif world == 2:
                        self.hardBlocks += [Block("RSC/Block/rockWall.png",
                                        [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                        (self.blockSize,self.blockSize))]
                    elif world == 3:
                        self.hardBlocks += [Block("RSC/Block/iceWall.png",
                                        [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                        (self.blockSize,self.blockSize))]
                    self.blocks += [self.hardBlocks[-1]]
                if c == "*":
                    if world == 1:    
                        self.blocks += [Block("RSC/Block/block.png",
                                    [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                    (self.blockSize,self.blockSize))]
                    elif world == 2:
                        self.blocks += [Block("RSC/Block/fireBlock.png",
                                    [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                    (self.blockSize,self.blockSize))]
                    elif world == 3:
                        self.blocks += [Block("RSC/Block/snowBlock.png",
                                    [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                    (self.blockSize,self.blockSize))]

        #----Done with file---
        try:
            thingfile = open(savedThingMap, "r")
        except (OSError, IOError) as e:
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
                    screen = "screen"
                    world = int(self.level[6])
                    levx = int(self.level[7])
                    levy = int(self.level[8])-1
                    newlev = screen + str(world) + str(levx) + str(levy)
                    self.levelChangeBlocks += [LevelChangeBlock(
                                                                "RSC/Block/NDoor.png",
                                                                [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                                                (self.blockSize, self.blockSize),
                                                                newlev, c)]
                if c == "n":
                    screen = "screen"
                    world = int(self.level[6])
                    levx = int(self.level[7])
                    levy = int(self.level[8])-1
                    newlev = screen + str(world) + str(levx) + str(levy)
                    self.levelChangeBlocks += [LevelChangeBlock(
                                                                "RSC/Block/EmptyDoor.png",
                                                                [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                                                (self.blockSize,self.blockSize),
                                                                newlev, c)]
                if c == "S":
                    screen = "screen"
                    world = int(self.level[6])
                    levx = int(self.level[7])
                    levy = int(self.level[8])+1
                    newlev = screen + str(world) + str(levx) + str(levy)
                    self.levelChangeBlocks += [LevelChangeBlock(
                                                                "RSC/Block/SDoor.png",
                                                                [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                                                (self.blockSize,self.blockSize),
                                                                newlev, c)]
                if c == "s":
                    screen = "screen"
                    world = int(self.level[6])
                    levx = int(self.level[7])
                    levy = int(self.level[8])+1
                    newlev = screen + str(world) + str(levx) + str(levy)
                    self.levelChangeBlocks += [LevelChangeBlock("RSC/Block/EmptyDoor.png",
                                                                [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                                                (self.blockSize,self.blockSize),
                                                                newlev, c)]
                if c == "W":
                    screen = "screen"
                    world = int(self.level[6])
                    levx = int(self.level[7])-1
                    levy = int(self.level[8])
                    newlev = screen + str(world) + str(levx) + str(levy)
                    self.levelChangeBlocks += [LevelChangeBlock(
                                                                "RSC/Block/WDoor.png",
                                                                [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                                                (self.blockSize,self.blockSize),
                                                                newlev, c)]
                if c == "w":
                    screen = "screen"
                    world = int(self.level[6])
                    levx = int(self.level[7])-1
                    levy = int(self.level[8])
                    newlev = screen + str(world) + str(levx) + str(levy)
                    self.levelChangeBlocks += [LevelChangeBlock(
                                                                "RSC/Block/EmptyDoor.png",
                                                                [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                                                (self.blockSize,self.blockSize),
                                                                newlev, c)]
                if c == "E":
                    screen = "screen"
                    world = int(self.level[6])
                    levx = int(self.level[7])+1
                    levy = int(self.level[8])
                    newlev = screen + str(world) + str(levx) + str(levy)
                    self.levelChangeBlocks += [LevelChangeBlock(
                                                                "RSC/Block/EDoor.png",
                                                                [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                                                (self.blockSize,self.blockSize),
                                                                newlev, c)]
                if c == "7":
                    if ((x*self.blockSize)+(self.blockSize/2) == self.blockSize/2 or
                        (x*self.blockSize)+(self.blockSize/2) == self.screenSize[0] -  self.blockSize/2 or
                        (y*self.blockSize)+(self.blockSize/2) == self.blockSize/2 or
                        (y*self.blockSize)+(self.blockSize/2) == self.screenSize[1] -  self.blockSize/2):
                            screen = "screen"
                            world = int(self.level[6])
                            levx = int(self.level[7])+1
                            levy = int(self.level[8])
                            newlev = screen + str(world) + str(levx) + str(levy)
                            self.doors += [Door(
                                                "RSC/Block/tree.png",
                                                [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                                (self.blockSize,self.blockSize),
                                                newlev, c)]
                    else:
                        self.keys += [Key(
                                            "RSC/Block/redKey.png",
                                            [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                            (self.blockSize,self.blockSize),
                                            c)]
                
                if c == "2":
                    if ((x*self.blockSize)+(self.blockSize/2) == self.blockSize/2 or
                        (x*self.blockSize)+(self.blockSize/2) == self.screenSize[0] -  self.blockSize/2 or
                        (y*self.blockSize)+(self.blockSize/2) == self.blockSize/2 or
                        (y*self.blockSize)+(self.blockSize/2) == self.screenSize[1] -  self.blockSize/2):
                            screen = "screen"
                            world = int(self.level[6])
                            levx = int(self.level[7])
                            levy = int(self.level[8])+1
                            newlev = screen + str(world) + str(levx) + str(levy)
                            self.doors += [Door(
                                                "RSC/Block/tree.png",
                                                [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                                (self.blockSize,self.blockSize),
                                                newlev, c)]
                    else:
                        self.keys += [Key(
                                            "RSC/Block/blueKey.png",
                                            [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                            (self.blockSize,self.blockSize),
                                            c)]
                if c == "3":
                    if ((x*self.blockSize)+(self.blockSize/2) == self.blockSize/2 or
                        (x*self.blockSize)+(self.blockSize/2) == self.screenSize[0] -  self.blockSize/2 or
                        (y*self.blockSize)+(self.blockSize/2) == self.blockSize/2 or
                        (y*self.blockSize)+(self.blockSize/2) == self.screenSize[1] -  self.blockSize/2):
                            screen = "screen"
                            world = int(self.level[6])
                            levx = int(self.level[7])+1
                            levy = int(self.level[8])
                            newlev = screen + str(world) + str(levx) + str(levy)
                            self.doors += [Door(
                                                "RSC/Block/tree.png",
                                                [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                                (self.blockSize,self.blockSize),
                                                newlev, c)]
                    else:
                        self.keys += [Key(
                                            "RSC/Block/yellowKey.png",
                                            [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                            (self.blockSize,self.blockSize),
                                            c)]
                if c == "e":
                    screen = "screen"
                    world = int(self.level[6])
                    levx = int(self.level[7])+1
                    levy = int(self.level[8])
                    newlev = screen + str(world) + str(levx) + str(levy)
                    self.levelChangeBlocks += [LevelChangeBlock(
                                                                "RSC/Block/EmptyDoor.png",
                                                                [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                                                (self.blockSize,self.blockSize),
                                                                newlev, c)]
                if c == "O":
                    screen = "screen"
                    world = int(self.level[6])
                    levx = int(self.level[7])+1
                    levy = int(self.level[8])
                    if world == 1:
                        world = 2
                        levx = 1
                        levy = 3
                    newlev = screen + str(world) + str(levx) + str(levy)
                    self.levelChangeBlocks += [LevelChangeBlock(
                                                                "RSC/Block/Portal.png",
                                                                [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)],
                                                                (self.blockSize,self.blockSize),
                                                                newlev, c)]

                if c == "G":
                    self.ghosts += [Ghost(
                                        [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)])]
                if c == "D":
                    self.demons += [Demon(
                                        [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)])]
                if c == "L":
                    self.leviathans += [Leviathan(
                                        [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)])]
                if c == "!":
                    self.pestilences += [Pestilence(
                                        [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)])]
                if c == "A":
                    self.wars += [War(
                                        [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)])]
                                        
                if c == "R":
                    self.deaths += [Death(
                                        [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)])]
                if c == "T":
                    self.pots += [Pot(
                                        [(x*self.blockSize)+(self.blockSize/2), (y*self.blockSize)+(self.blockSize/2)])]
