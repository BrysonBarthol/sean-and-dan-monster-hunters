import pygame, math, sys
from HUD import Text
from Player import Player

class HUDHearts():
    def __init__(self, pos, player):
        self.player = player
        self.maxHearts = self.player.maxHealth/3
        self.images = []
        for i in range(13):
            self.images += [pygame.image.load("RSC\HUD\health" + str(i) + ".png")]
        self.image = self.images[self.player.health]
        self.rect = self.image.get_rect()
        self.place(pos)
        
        
    def place(self, pos):
        self.rect.topleft = pos
        
    def update(self):
        if 0 <= self.player.health <= 12: 
            self.image = self.images[self.player.health]
    
