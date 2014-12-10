import pygame, math
from Creature import Creature

class Demon(Creature):
	def __init__(self, pos):
		Creature.__init__(self, "RSC/Demon/DemonUp1.png", [0,0], pos)
		self.upImages = [pygame.image.load("RSC/Demon/DemonUp1.png"),
							pygame.image.load("RSC/Demon/DemonUp2.png")]
		self.downImages = [pygame.image.load("RSC/Demon/DemonDown1.png"),
							pygame.image.load("RSC/Demon/DemonDown2.png")]
		self.leftImages = [pygame.image.load("RSC/Demon/DemonLeft1.png"),
							pygame.image.load("RSC/Demon/DemonLeft2.png")]
		self.rightImages = [pygame.image.load("RSC/Demon/DemonRight1.png"),
							pygame.image.load("RSC/Demon/DemonRight2.png")]]
		self.facing = "down"
		self.changed = False
		self.images = self.downImages
		self.frame = 0
		self.maxFrame = len(self.images) - 1
		self.waitCount = 0
		self.maxWait = 60*.25
		self.image = self.images[self.frame]
		self.rect = self.image.get_rect(center = self.rect.center)
		self.maxSpeed = 10
		self.detectRadius = 32 #Play with this number
	
	def update(self, player, width, height):
		self.detectPlayer(player)
		Creature.update(self, width, height)
		self.animate()
		self.changed = False
		
	def collidePlayer(self, other):
		pass
		
	def collideDemon(self, other):
		if self.rect.left < 0 or self.rect.right > width:
				self.didBounceX = False
			if self.rect.top < 0 or self.rect.bottom > height:
				self.didBounceY = False
				
	def collideLeviathan(self, other):
		if self.rect.left < 0 or self.rect.right > width:
				self.didBounceX = False
			if self.rect.top < 0 or self.rect.bottom > height:
				self.didBounceY = False
				
	def collideBlock(self, other):
			if self.rect.left < 0 or self.rect.right > width:
				self.didBounceX = False
			if self.rect.top < 0 or self.rect.bottom > height:
				self.didBounceY = False
				
	def detectPlayer(self, player):
		if self.direction == "up"
			if self.rect.right+self.detectRadius > player.rect.left:
				if self.rect.left-self.detectRadius < player.rect.right:
					if self.rect.bottom > player.rect.top:
						if self.rect.top-self.detectRadius*2 < other.rect.bottom:
							seen = True
		if self.direction == "down"
			if self.rect.right+self.detectRadius > player.rect.left:
				if self.rect.left-self.detectRadius < player.rect.right:
					if self.rect.bottom+self.detectRadius*2 > player.rect.top:
						if self.rect.top < other.rect.bottom:
							seen = True
		if self.direction == "right"
			if self.rect.right+self.detectRadius > player.rect.left:
				if self.rect.left-self.detectRadius < player.rect.right:
					if self.rect.bottom+self.detectRadius*2 > player.rect.top:
						if self.rect.top < other.rect.bottom:
							seen = True
		if self.direction == "left"
			if self.rect.right+self.detectRadius > player.rect.left:
				if self.rect.left-self.detectRadius < player.rect.right:
					if self.rect.bottom+self.detectRadius*2 > player.rect.top:
						if self.rect.top < other.rect.bottom:
							seen = True
