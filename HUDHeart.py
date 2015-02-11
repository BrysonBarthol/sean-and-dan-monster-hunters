import pygame, math, sys
from HUD import Text
from Player import Player

class HUDHearts():
    def __init__(self, pos, player):
        self.player = player
        self.maxHearts = self.player.maxHealth/3
        self.setImages(self)
        self.place(pos)
        self.heart_3 = pygame.image.load("RSC/HUD/heart3.png")
        self.heart_2 = pygame.image.load("RSC/HUD/heart2.png")
        self.heart_1 = pygame.image.load("RSC/HUD/heart1.png")
        self.heart_0 = pygame.image.load("RSC/HUD/heart0.png")
        self.heart_1_3 = pygame.image.load("RSC/HUD/heart1.3.png")
        self.heart_2_3 = pygame.image.load("RSC/HUD/heart2.3.png")
        
        
    def place(self, pos):
        self.rect.topleft = tos
        
    def setImages(self):
        if self.player.health == 12:
            self.images = [self.heart_3, self.heart_1]
        elif self.player.health == 11:
            self.images = [self.heart_3, self.heart_2_3]
        elif self.player.health == 10:
            self.images = [self.heart_3, self.heart_1_3]
        elif self.player.health == 9:
            self.images = [self.heart_2, self.heart_1]
        elif self.player.health == 8:
            self.images = [self.heart_2, self.heart_2_3]
        elif self.player.health == 7:
            self.images = [self.heart_2, self.heart_1_3]
        elif self.player.health == 6:
            self.images = [self.heart_1, self.heart_1]
        elif self.player.health == 5:
            self.images = [self.heart_1, self.heart_2_3]
        elif self.player.health == 4:
            self.images = [self.heart_1, self.heart_1_3]
        elif self.player.health == 3:
            self.images = [self.heart_1, self.heart_0]
        elif self.player.health == 2:
            self.images = [self.heart_2_3, self.heart_0]
        elif self.player.health == 1:
            self.images = [self.heart_1_3, self.heart_0]
        elif self.player.health == 0:
            self.images = [self.heart_0, self.heart_0]
        self.rects
