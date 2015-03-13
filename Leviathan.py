import pygame, math
from Demon import Demon
from Creature import Creature
from Bullet import Bullet
from Player import Player


class Leviathan(Demon):
    def __init__(self, pos):
        image = ("RSC/Leviathan/LeviUp1.png")
        self.seen = False
        Demon.__init__(self,pos)
        self.speedx = 1
        self.speedy = 0
        self.oldSpeedx = 1
        self.oldSpeedy = 0
        self.upImages = [pygame.image.load("RSC/Leviathan/LeviUp1.png"),
                            pygame.image.load("RSC/Leviathan/LeviUp2.png")]
        self.downImages = [pygame.image.load("RSC/Leviathan/LeviDown1.png"),
                            pygame.image.load("RSC/Leviathan/LeviDown2.png")]
        self.leftImages = [pygame.image.load("RSC/Leviathan/LeviLeft1.png"),
                            pygame.image.load("RSC/Leviathan/LeviLeft2.png")]
        self.rightImages = [pygame.image.load("RSC/Leviathan/LeviRight1.png"),
                            pygame.image.load("RSC/Leviathan/LeviRight2.png")]
        self.upHurtImages = [pygame.image.load("RSC/Leviathan/LeviUpHit1.png"),
                             pygame.image.load("RSC/Leviathan/LeviUpHit2.png")]
        self.downHurtImages = [pygame.image.load("RSC/Leviathan/LeviDownHit1.png"),
                            pygame.image.load("RSC/Leviathan/LeviDownHit2.png")]
        self.leftHurtImages = [pygame.image.load("RSC/Leviathan/LeviLeftHit1.png"),
                            pygame.image.load("RSC/Leviathan/LeviLeftHit2.png")]
        self.rightHurtImages = [pygame.image.load("RSC/Leviathan/LeviRightHit1.png"),
                            pygame.image.load("RSC/Leviathan/LeviRightHit2.png")]
        self.images = self.downImages
        self.image = self.images[self.frame]
        self.shooting = False
        self.shootDelay = 0
        self.maxShootDelay = 50
        self.bullet = 0
        self.health = 3
        
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
       
    def update(self, width, height, players):
        Demon.update(self, width, height, players)
        for player in players:
            self.detect(player)
        
        if self.shooting:
            return self.shoot()
            if self.bullet > 1:
                self.shootDelay = self.maxShootDelay
                return []
        else:
            return []
            
        
    def move(self, players):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
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
    
    def shoot(self, command = ""):
        return [Bullet(self.rect.center, self.facing, 10)]
        self.bullet += 1
        
    #The following code was written (partly) by Dominic Flanders
    
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
            
            if not self.shooting:
                self.oldSpeedx = self.speedx
                self.oldSpeedy = self.speedy
                self.speedx = 0
                self.speedy = 0
            
            if math.fabs(pX-zX) > math.fabs(pY-zY):
                if pX > zX:
                    self.facing = "right"
                    self.shooting = True
                    
                else:
                    self.facing = "left"
                    self.shooting = True
            else:
                if pY > zY:
                    self.facing = "down"
                    self.shooting = True
                else:
                    self.facing = "up"
                    self.shooting = True
        else:
            if self.shooting:
                self.speedx = self.oldSpeedx
                self.speedy = self.oldSpeedy
            self.shooting = False    
          
          
