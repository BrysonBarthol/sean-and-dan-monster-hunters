import pygame, math, sys
from Creature import Creature

class Pot(Creature):
    def __init__(self, pos):
        image = ("RSC/Block/Pot1.png")
        Creature.__init__(self, "RSC/Block/Pot1.png", [0,0], pos)
        self.speedx = 0
        self.speedy = 0
        self.upImages = [pygame.image.load("RSC/Block/Pot1.png")]
        self.upHurtImages = [pygame.image.load("RSC/Block/Pot2.png"),
                             pygame.image.load("RSC/Block/Pot3.png")]
        self.health = 1
        self.facing = "up"
        self.changed = False
        self.waitCount = 0
        self.maxWait = 60*.25
        self.images = self.upImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = self.rect.center)
                             
    def update(self, width, height):
        Creature.update(self, width, height)
        self.changed = False



        
    

