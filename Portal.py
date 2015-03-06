import pygame, math, sys, time, os
from Block import Block

class Portal(Block):
    def __init__(self, image, pos, size):
        self.Image = pygame.image.load("RSC/Block/portal.png")
