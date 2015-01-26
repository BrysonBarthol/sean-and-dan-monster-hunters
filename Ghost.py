import pygame, math
from Creature import Creature

class Ghost(Creature):
    def __init__(self, pos):
        image = ("RSC/Ghost/GhostUp1.png")
        speed = [1,1]
        Creature.__init__(self, image, speed, pos)
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
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = self.rect.center)
        self.maxSpeed = 2
        
    def update(self, width, height):
        Creature.update(self, width, height)
        self.animate()
        self.changed = False
        
    def collidePlayer(self, other): #do damage, don't bounce
        if self != other:
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        pass
                        #hurt(player) OR player.hurt = True?
        
    def collideDemon(self, other):
        if self != other:
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        if not self.didBounceX:
                            self.speedx = -self.speedx
                            self.didBouncex = False
                        if not self.didBounceY:
                            self.speedy = -self.speedy
                            self.didBounceY = False
                
    def collideLeviathan(self, other):
        if self != other:
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        if not self.didBounceX:
                            self.speedx = -self.speedx
                            self.didBouncex = False
                        if not self.didBounceY:
                            self.speedy = -self.speedy
                            self.didBounceY = False
                
    def collideBlock(self, width, height):
        if not self.didBounceX:
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = -self.speedx
                self.didBounceX = False
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = -self.speedy
                self.didBounceY = False
        
    def collideWall(self, width, height):
        if not self.didBounceX:
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = -self.speedx
                self.didBounceX = True
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = -self.speedy
                self.didBounceY = True
                
    #def go(self, direction):
        if direction == "up":
            self.facing = "up"
            self.changed = True
        if direction == "down":
            self.facing = "down"
            self.changed = True
        if direction == "left":
            self.facing = "left"
            self.changed = True
        if direction == "right":
            self.facing = "right"
            self.changed = True                
