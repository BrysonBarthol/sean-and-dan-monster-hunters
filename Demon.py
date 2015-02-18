import pygame, math
from Creature import Creature
from Player import Player

class Demon(Creature):
    def __init__(self, pos):
        Creature.__init__(self, "RSC/Demon/DemonDown1.png", [0,0], pos)
        self.speedx = 0
        self.speedy = 2
        self.upImages = [pygame.image.load("RSC/Demon/DemonUp1.png"),
                            pygame.image.load("RSC/Demon/DemonUp2.png")]
        self.downImages = [pygame.image.load("RSC/Demon/DemonDown1.png"),
                            pygame.image.load("RSC/Demon/DemonDown2.png")]
        self.leftImages = [pygame.image.load("RSC/Demon/DemonLeft1.png"),
                            pygame.image.load("RSC/Demon/DemonLeft2.png")]
        self.rightImages = [pygame.image.load("RSC/Demon/DemonRight1.png"),
                            pygame.image.load("RSC/Demon/DemonRight2.png")]
        self.seen = False
        self.direction = "down"
        self.changed = False
        self.images = self.downImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = self.rect.center)
        self.maxSpeed = 2
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.detectionRadius = 96
        self.shooting = False
            
        if math.fabs(self.speedx) >= math.fabs(self.speedy):
                if self.speedx >= 0:
                    self.facing = "right"
                else:
                    self.facing = "left"
        else:
            if self.speedy >= 0:
                self.facing = "down"
            else:
                self.facing = "up"
    
    def move(self, players):
        for player in players:
            self.detect(player)
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
    
    def update(self, width, height, players):
        if self.didBounceX or self.didBounceY:
            self.changed = True
        if math.fabs(self.speedx) >= math.fabs(self.speedy):
            if self.speedx >= 0:
                self.facing = "right"
            else:
                self.facing = "left"
        else:
            if self.speedy >= 0:
                self.facing = "down"
            else:
                self.facing = "up"            
        self.move(players)
        self.collideWall(width, height)
        self.animate()
        self.changed = False
        self.didBounceX = False
        self.didBounceY = False
        
        
    def collidePlayer(self, other):
        hurt(player)
        
    def collideDemon(self, other):
        if self != other:
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        if not self.didBounceX:
                            self.speedx = -self.speedx
                            self.didBouncex = True
                        if not self.didBounceY:
                            self.speedy = -self.speedy
                            self.didBounceY = True
    
    def collideLeviathan(self, other):          
        if self != other:
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        if not self.didBounceX:
                            self.speedx = -self.speedx
                            self.didBouncex = True
                        if not self.didBounceY:
                            self.speedy = -self.speedy
                            self.didBounceY = True
    
    #The following code was written by Dominic Flanders
    
    def distToPoint(self, pt):
        x1 = self.rect.center[0]
        x2 = pt[0]
        y1 = self.rect.center[1]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
                
    def detect(self, player):
        if self.distToPoint(player.rect.center) < self.detectionRadius:
            pX = player.rect.center[0]
            pY = player.rect.center[1]
            zX = self.rect.center[0]
            zY = self.rect.center[1]
           
            if pX > zX:
                self.speedx = self.maxSpeed
            elif pX < zX:
                self.speedx = -self.maxSpeed
            else:
                self.speedx = 0
       
            if pY > zY:
                self.speedy = self.maxSpeed
            elif pY < zY:
                self.speedy = -self.maxSpeed
            else:
                self.speedy = 0
                
        
        
