import pygame, math
from Leviathan import Leviathan
from Ghost import Ghost

class Boss(Leviathan, Ghost):
	def __init__(self, pos):
		Leviathin.__init__(self, pos)
		Ghost.__init__(self, pos)
		self.upImages = [pygame.image.load("RSC/Boss/BossUp2.png"),
						 pygame.image.load("RSC/Boss/BossUp2.png")]
		self.downImages = [pygame.image.load("RSC/Boss/BossDown1.png"),
							pygame.image.load("RSC/Boss/BossDown2.png")]
		self.leftImages = [pygame.image.load("RSC/Boss/BossLeft1.png"),
							pygame.image.load("RSC/Boss/BossLeft2.png")]
		self.rightImages = [pygame.image.load("RSC/Boss/BossRight1.png"),
							pygame.image.load("RSC/Boss/BossRight2.png")]]
		
		
		self.detectRadius = 50 #Play with the number
	

		


