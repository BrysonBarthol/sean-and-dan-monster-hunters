import pygame, math, sys
from HUD import Text

class HUDHearts():
        def __init__(self, pos):
                hearts = 3
                self.image = setImage()
                self.rect = self.image.get_rect(center = self.rect.center)
                self.change = False
                self.place(self, pos)        
        
        def setImage(self):
            if hearts == 1: 
                pygame.image.load("RSC/HUD/heart1.png")
            elif hearts == 2:
                pygame.image.load("RSC/HUD/heart2.png")
            elif hearts == 3:
                pygame.image.load("RSC/HUD/heart3.png")
            elif hearts == 4:
                pygame.image.load("RSC/HUD/heart4.png")

        def place(self, pos):
            self.rect.center = pos
             
        def update(self):
                if self.change:
                        self.image = 
                        self.rect = self.image.get_rect(center = self.rect.center)
                        self.change = False
        
        def setHearts(self, hearts):
                self.hearts = hearts
                self.change = True
                
        def increaseHearts(self, amount = 1):
                self.hearts += amount
                self.change = True
                
        def decreaseHearts(self, amount = -1):
                self.hearts += amount
                self.change = True
                
        def resetHearts(self):
                self.hearts = 3
                self.change = True
