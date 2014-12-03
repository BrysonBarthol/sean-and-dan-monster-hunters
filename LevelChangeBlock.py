import pygame, math, sys
from Block import Block

class LevelChangeBlock(Block):
    def __init__(self, dest, pos = [0,0], size = [100,100]):
		Block.__init__(self, "RSC/Block/LevelChangeBlock.png", pos, size)
		self.dest = dest
		
