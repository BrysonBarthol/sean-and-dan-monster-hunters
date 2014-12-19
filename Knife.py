import pygame, math

class Knife():
	def __init__(self, pos, direction, damage):
		self.image = pygame.image.load("RSC/weapons/bullet.png")
		self.rect = self.image.get_rect()
		speed = 5
		if facing == "up":
			self.offsetx=0
			self.offsety=4
		elif facing == "down":
			self.offsetx=0
			self.offsety=-4
		elif facing == "right":
			self.offsetx=4
			self.offsety=0
		elif facing == "up":
			self.offsetx=-4
			self.offsety=0
		self.place(pos)
		self.living = True
		self.damage = 1
		
	def place(self, pos):
		self.rect.center = pos
		
	def update(self, width, height):
		self.move()
		self.collideWall(width, height)
		
	def collideWall(self, width, height):
		pass
		
	def collideBall(self, other):
		if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
			if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
				if (self.radius + other.radius) > self.distance(other.rect.center):
					self.living = False
