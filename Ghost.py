import pygame
from Creature import Creature

class Ghost(Creature):
	def __init__(self, "RSC/Ghost/gDown1.png", [0,0], pos):
		self.upImages = [pygame.image.load("RSC/Ghost/gUp1.png"),
							pygame.image.load("RSC/Ghost/gUp2.png")]
		self.downImages = [pygame.image.load("RSC/Ghost/gDown1.png"),
							pygame.image.load("RSC/Ghost/gDown2.png")]
		self.leftImages = [pygame.image.load("RSC/Ghost/gLeft1.png"),
							pygame.image.load("RSC/Ghost/gLeft2.png")]
		self.rightImages = [pygame.image.load("RSC/Ghost/gRight1.png"),
							pygame.image.load("RSC/Ghost/gRight2.png")]
		self.facing = "down"
		self.changed = False
		self.images = self.downImages
		self.frame = 0
		#self.maxFrame = len(self.images) - 1
		self.waitCount = 0
		self.maxWait = 60*.25
		self.image = self.images[self.frame]
		self.rect = self.image.get_rect(center = self.rect.center)
		self.maxSpeed = 10
		
	def update(self, width, height):
		Creature.update(self, width, height)
		self.animate()
		self.changed = False
		
	def collidePlayer(self, other):
		
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
		
	def animate(self):
		if self.waitCount < self.maxWait:
			self.waitCount += 1
		else:
			self.waitCount = 0
			self.changed = True
			if self.frame < self.maxFrame:
				self.frame += 1
			else:
				self.frame = 0
		
		if self.changed:	
			if self.facing == "up":
				self.images = self.upImages
			elif self.facing == "down":
				self.images = self.downImages
			elif self.facing == "right":
				self.images = self.rightImages
			elif self.facing == "left":
				self.images = self.leftImages
			
			self.image = self.images[self.frame]
