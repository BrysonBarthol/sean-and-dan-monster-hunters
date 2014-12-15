import pygame, math
from Demon import Demon


class Leviathan(Demon):
	def __init__(self, pos):
		Creature.__init__(self, "RSC/Leviathan/LeviDown1.png", [0,0], pos)
		self.upImages = [pygame.image.load("RSC/Leviathan/LeviUp1.png"),
							pygame.image.load("RSC/Leviathan/LeviUp2.png")]
		self.downImages = [pygame.image.load("RSC/Leviathan/LeviDown1.png"),
							pygame.image.load("RSC/Leviathan/LeviDown2.png")]
		self.leftImages = [pygame.image.load("RSC/Leviathan/LeviLeft1.png"),
							pygame.image.load("RSC/Leviathan/LeviLeft2.png")]
		self.rightImages = [pygame.image.load("RSC/Leviathan/LeviRight1.png"),
							pygame.image.load("RSC/Leviathan/LeviRight2.png")]
							
	def seen(self, player):
