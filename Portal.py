import pygame, math, sys
from Block import Block

class Portal(Block):
    def __init__(self, pos):
        self.image = pygame.image.load("RSC/Block/portal.png")
        size = pygame.image.size
        Block.__init__(self, self.image, pos, size)
        if size != None:
            self.resize(size)
        else:
            self.image = self.baseImage
        
