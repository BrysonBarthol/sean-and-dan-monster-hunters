import pygame, math, sys
from Block import Block

class Door(Block):
    def __init__(self,img, pos, size, newlev, kind):
        Block.__init__(self, img, pos, size)
        self.img = img
        print newlev
        self.newlev = newlev
        self.kind = kind


    def playerCollide(self, other):
        if (self.rect.right > other.rect.left
            and self.rect.left < other.rect.right):
            if (self.rect.bottom > other.rect.top and
                self.rect.top < other.rect.bottom):
                    if self.kind in other.keys:
                        print "I'm going to ", self.newlev
                        return True
                    else:
                        other.go("stop")
        return False

