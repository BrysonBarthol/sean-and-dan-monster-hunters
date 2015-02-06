import pygame, math, sys
from HUD import Text
from Player import Player

class HUDHearts():
    def __init__(self, pos, player):
        self.player = player
        self.maxHearts = self.player.maxHealth/3
        self.setImages(self)
        self.place(pos)
        self.heart_3 = pygame.image.load("RSC/HUD/heart3.png"
        self.heart_2 = pygame.image.load("RSC/HUD/heart2.png"
        self.heart_1 = pygame.image.load("RSC/HUD/heart1.png"
        self.heart_0 = pygame.image.load("RSC/HUD/heart1.png"
        self.heart_1-3 = pygame.image.load("RSC/HUD/heart1.3.png"
        self.heart_2-3 = pygame.image.load("RSC/HUD/heart2.3.png"
        
        
    def place(self, pos):
        pass
        
    def setImages(self):
        if self.player.health == 12:
            self.images = 
