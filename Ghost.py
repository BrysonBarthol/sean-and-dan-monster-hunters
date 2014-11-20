import pygame
from Creature import Creature

class Ghost(Creature):
	def __init__():
	self.upImages = [pygame.image.load("RSC/Ghost/gUp1.png"),
						pygame.image.load("RSC/Ghost/gUp2.png")]
	self.downImages = [pygame.image.load("RSC/Ghost/gDown1.png"),
						pygame.image.load("RSC/Ghost/gDown2.png")]
	self.leftImages = [pygame.image.load("RSC/Ghost/gLeft1.png"),
						pygame.image.load("RSC/Ghost/gLeft2.png")]
	self.rightImages = [pygame.image.load("RSC/Ghost/gRight1.png"),
						pygame.image.load("RSC/Ghost/gRight2.png")]
