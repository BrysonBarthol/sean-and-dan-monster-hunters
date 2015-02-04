import pygame, math
from Demon import Demon
from Bullet import Bullet
from Player import Player


class Leviathan(Demon):
    def __init__(self, pos):
        image = ("RSC/Leviathan/LeviUp1.png")
        speed = [1,0]
        Demon.__init__(self, "RSC/Leviathan/LeviDown1.png", speed, pos)
        self.upImages = [pygame.image.load("RSC/Leviathan/LeviUp1.png"),
                            pygame.image.load("RSC/Leviathan/LeviUp2.png")]
        self.downImages = [pygame.image.load("RSC/Leviathan/LeviDown1.png"),
                            pygame.image.load("RSC/Leviathan/LeviDown2.png")]
        self.leftImages = [pygame.image.load("RSC/Leviathan/LeviLeft1.png"),
                            pygame.image.load("RSC/Leviathan/LeviLeft2.png")]
        self.rightImages = [pygame.image.load("RSC/Leviathan/LeviRight1.png"),
                            pygame.image.load("RSC/Leviathan/LeviRight2.png")]                   
        self.images = self.downImages
        self.image = self.images[self.frame]
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
    
    def shoot(self):
        return Bullet(self.rect.center, self.facing)
        self.changed = True
        self.shooting = True
                            
    def detectPlayer(self, player):
        if seen:
            if xdiff > 0: #to the right of the player
                self.speed = 0
                self.facing = "right"
            elif xdiff < 0: #to the left
                self.speed = 0
                self.facing = "left"
                
            if ydiff > 0: #below
                self.speed = 0
                self.facing = "down"
            elif ydiff < 0: #above
                self.speed = 0
                self.facing = "up"
            
                shoot()
            
            
