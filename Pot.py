import pygame, math, sys
from Block import Block

class Pot(Block):
    def __init__(self,img, pos, size, newlev, kind):
        Block.__init__(self, img, pos, size)
        self.img = pygame.load.image("RSC/


    def playerCollide(self, other):
        if (self.rect.right > other.rect.left
            and self.rect.left < other.rect.right):
            if (self.rect.bottom > other.rect.top and
                self.rect.top < other.rect.bottom):
                return True
        return False

