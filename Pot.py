import pygame, math, sys
from Creature import Creature

class Pot(Creature):
    def __init__(self, pos):
        image = ("RSC/Block/Pot1.png")
        Creature.__init__(self, "RSC/Block/Pot1.png", [0,0], pos)
        self.speedx = 0
        self.speedy = 0
        self.upImages = [pygame.image.load("RSC/Block/Pot1.png")]
        self.upHurtImages = [pygame.image.load("RSC/Block/Pot2.png"),
                             pygame.image.load("RSC/Block/Pot3.png")]
        self.health = 1
        self.facing = "up"
        self.changed = False
        
        self.images = self.upImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = self.rect.center)
                             
    def update(self, width, height):
        Creature.update(self, width, height)
        self.changed = False
        
    #def collidePlayer(self, other):
        #if self != other:
            #if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                #if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    #if (self.radius + other.radius) > self.distance(other.rect.center):
                        #print "Collided"
                        
        
    #def collideDemon(self, other):
        #if self != other:
            #if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                #if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    #if (self.radius + other.radius) > self.distance(other.rect.center):
                        #if not self.didBounceX:
                            #self.speedx = -self.speedx
                            #self.didBouncex = False
                        #if not self.didBounceY:
                            #self.speedy = -self.speedy
                            #self.didBounceY = False
                
    #def collideLeviathan(self, other):
        #if self != other:
            #if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                #if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    #if (self.radius + other.radius) > self.distance(other.rect.center):
                        #if not self.didBounceX:
                            #self.speedx = -self.speedx
                            #self.didBouncex = False
                        #if not self.didBounceY:
                            #self.speedy = -self.speedy
                            #self.didBounceY = False
        









#class Pot():
    #def __init__(self, pos = [0,0]):
        #Block.__init__(self, image, pos)
        #self.image = self.baseImage
        #self.image = pygame.image.load("RSC/Block/Pot1.png")
        #self.hitImages = [pygame.image.load("RSC/Block/Pot2.png"),
        #                     pygame.image.load("RSC/Block/Pot3.png")]
        #self.rect = self.image.get_rect()
        #self.place(pos)
        #self.hit = False
    
    #def place(self, pos):
        #self.rect.center = pos
    
    #def distance(self, pt):
        #x1 = self.rect.center[0]
        #y1 = self.rect.center[0]
        #y2 = pt[0]
        #x2 = pt[0]
        #return math.sqrt (((x2-x1)**2) + ((y2-y1)**2))
    
    #def collideBullet(self, other):
        #if self != other:
            #if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                #if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    #if (self.radius + other.radius) > self.distance(other.rect.center):
                        #self.hit = True
                        
    #def update(self, width, height):
        
    

