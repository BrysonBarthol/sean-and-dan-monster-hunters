import pygame
from Creature import Creature

class Player(Creature):
	def __init__(self, pos):
		Creature.__init__(self, "RSC/Player/PlayerUp2.png", [0,0], pos)
		self.upImages = [pygame.image.load(image),
						 pygame.image.load(image)]
		self.downImages = [pygame.image.load(image),
						   pygame.image.load(image)]
		self.leftImages = [pygame.image.load(image),
						   pygame.image.load(image)]
		self.rightImages = [pygame.image.load(image),
						    pygame.image.load(image)]
		self.upImagesRanged = [pygame.image.load(image),
						 pygame.image.load(image)]
		self.downImagesRanged = [pygame.image.load(image),
						   pygame.image.load(image)]
		self.leftImagesRanged = [pygame.image.load(image),
						   pygame.image.load(image)]
		self.rightImagesRanged = [pygame.image.load(image),
						    pygame.image.load(image)]
		self.upImagesSalt = [pygame.image.load(image),
						 pygame.image.load(image)]
		self.downImagesSalt = [pygame.image.load(image),
						   pygame.image.load(image)]
		self.leftImagesSalt = [pygame.image.load(image),
						   pygame.image.load(image)]
		self.rightImagesSalt = [pygame.image.load(image),
						    pygame.image.load(image)]
		self.upImagesKnife = [pygame.image.load(image),
						 pygame.image.load(image)]
		self.downImagesKnife = [pygame.image.load(image),
						   pygame.image.load(image)]
		self.leftImagesKnife = [pygame.image.load(image),
						   pygame.image.load(image)]
		self.rightImagesKnife = [pygame.image.load(image),
						    pygame.image.load(image)]
		self.facing = "up"
		self.changed = False
		self.images = self.upImages
		self.frame = 0
		self.maxFrame = len(self.images) - 1
		self.waitCount = 0
		self.maxWait = 60*.25
		self.image = self.images[self.frame]
		self.rect = self.image.get_rect(center = self.rect.center)
		self.maxSpeed = 10
			
	def update(self, width, height):
		Creature.update(self, width, height)
		self.animate()
		self.changed = False
		
	def collideWall(self, width, height):
		if not self.didBounceX:
			#print "trying to hit Wall"
			if self.rect.left < 0 or self.rect.right > width:
				self.speedx = 0
				self.didBounceX = True
				#print "hit xWall"
		if not self.didBounceY:
			if self.rect.top < 0 or self.rect.bottom > height:
				self.speedy = 0
				self.didBounceY = True
				#print "hit xWall"
	
	
	def animateRanged(self):
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
				self.images = self.upImagesRanged
			elif self.facing == "down":
				self.images = self.downImagesRanged
			elif self.facing == "right":
				self.images = self.rightImagesRanged
			elif self.facing == "left":
				self.images = self.leftImagesRanged
			
			self.image = self.images[self.frame]
			
	def animateSalt(self):
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
				self.images = self.upImagesSalt
			elif self.facing == "down":
				self.images = self.downImagesSalt
			elif self.facing == "right":
				self.images = self.rightImagesSalt
			elif self.facing == "left":
				self.images = self.leftImagesSalt
			
			self.image = self.images[self.frame]
			
	def animateKnife(self):
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
				self.images = self.upImagesSalt
			elif self.facing == "down":
				self.images = self.downImagesSalt
			elif self.facing == "right":
				self.images = self.rightImagesSalt
			elif self.facing == "left":
				self.images = self.leftImagesSalt
			
			self.image = self.images[self.frame]
	
	def go(self, direction):
		if direction == "up":
			self.facing = "up"
			self.changed = True
			self.speedy = -self.maxSpeed
		elif direction == "stop up":
			self.speedy = 0
		elif direction == "down":
			self.facing = "down"
			self.changed = True
			self.speedy = self.maxSpeed
		elif direction == "stop down":
			self.speedy = 0
			
		if direction == "right":
			self.facing = "right"
			self.changed = True
			self.speedx = self.maxSpeed
		elif direction == "stop right":
			self.speedx = 0
		elif direction == "left":
			self.facing = "left"
			self.changed = True
			self.speedx = -self.maxSpeed
		elif direction == "stop left":
			self.speedx = 0





