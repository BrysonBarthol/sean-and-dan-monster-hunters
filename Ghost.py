import pygame
from Creature import Creature

class Ghost(Creature):
	def __init__(self, pos):
		Creature.__init__(self, image, speed = [0,0], pos = [0,0])
		self.upImages = [pygame.image.load("RSC/Ghost/GhostUp1.png"),
							pygame.image.load("RSC/Ghost/GhostUp2.png")]
		self.downImages = [pygame.image.load("RSC/Ghost/GhostDown1.png"),
							pygame.image.load("RSC/Ghost/GhostDown2.png")]
		self.leftImages = [pygame.image.load("RSC/Ghost/GhostLeft1.png"),
							pygame.image.load("RSC/Ghost/GhostLeft2.png")]
		self.rightImages = [pygame.image.load("RSC/Ghost/GhostRight1.png"),
							pygame.image.load("RSC/Ghost/GhostRight2.png")]
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
