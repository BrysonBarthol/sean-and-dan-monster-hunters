import pygame, math, sys
from Block import Block

class LevelChangeBlock(Block):
    def __init__(self, pos, size, newMap):
        Block.__init__(self, "RSC/Block/LevelChangeBlock.png", pos, size)
        self.newMap = newMap


    def playerCollide(self, other):
        if (self.rect.right > other.rect.left
            and self.rect.left < other.rect.right):
            if (self.rect.bottom > other.rect.top and
                self.rect.top < other.rect.bottom):
                print "I'm going to ", self.newMap
                return True
        return False


