import pygame, math
from Creature import Creature

class Demon(Creature):
	def __init__(self, pos, speed = [0,0]):
	self.upImages = [pygame.image.load("RSC/Demon/dUp1.png"),
						pygame.image.load("RSC/Demon/dUp2.png")]
	self.downImages = [pygame.image.load("RSC/Demon/dDown1.png"),
						pygame.image.load("RSC/Demon/dDown2.png")]
	self.leftImages = [pygame.image.load("RSC/Demon/dLeft1.png"),
						pygame.image.load("RSC/Demon/dLeft2.png")]
	self.rightImages = [pygame.image.load("RSC/Demon/dRight1.png"),
						pygame.image.load("RSC/Demon/dRight2.png")]
