import pygame, math
from Demon import Demon

class Leviathan(Demon):
	def __init__(self, "RSC/Leviathan/lDown1.png", [0,0], pos):
	self.upImages = [pygame.image.load("RSC/Leviathan/lUp1.png"),
						pygame.image.load("RSC/Leviathan/lUp2.png")]
	self.downImages = [pygame.image.load("RSC/Leviathan/lDown1.png"),
						pygame.image.load("RSC/Leviathan/lDown2.png")]
	self.leftImages = [pygame.image.load("RSC/Leviathan/lLeft1.png"),
						pygame.image.load("RSC/Leviathan/lLeft2.png")]
	self.rightImages = [pygame.image.load("RSC/Leviathan/lRight1.png"),
						pygame.image.load("RSC/Leviathan/lRight2.png")]
