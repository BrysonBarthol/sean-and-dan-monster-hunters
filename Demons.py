import pygame, math
from Creature import Creature

class Demon(Creature):
	def __init__(self, pos):
		Creature.__init__(self, image, speed = [0,0], pos = [0,0])
		self.upImages = [pygame.image.load("RSC/Demon/DemonUp1.png"),
							pygame.image.load("RSC/Demon/DemonUp2.png")]
		self.downImages = [pygame.image.load("RSC/Demon/DemonDown1.png"),
							pygame.image.load("RSC/Demon/DemonDown2.png")]
		self.leftImages = [pygame.image.load("RSC/Demon/DemonLeft1.png"),
							pygame.image.load("RSC/Demon/DemonLeft2.png")]
		self.rightImages = [pygame.image.load("RSC/Demon/DemonRight1.png"),
							pygame.image.load("RSC/Demon/DemonRight2.png")]]
		
