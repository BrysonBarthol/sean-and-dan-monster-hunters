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
        self.images = self.downImages
        self.image = self.images[self.frame]
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
    
   # def update(self, players, width, height):
      #  self.speed = [self.speedx, self.speedy]
      #  if self.didBounceX or self.didBounceY:
         #   self.changed = True
      #  if math.fabs(self.speedx) >= math.fabs(self.speedy):
        #    if self.speedx >= 0:
         #       self.facing = "right"
        #    else:
          #      self.facing = "left"
       # else:
        #    if self.speedy >= 0:
        #        self.facing = "down"
        #    else:
         #       self.facing = "up"    
        #Creature.update(self, width, height)
        #self.move(players)
        #self.collideWall(width, height)
       # self.animate()
        #self.changed = False
       
    def update(self, width, height, players):
        Demon.update(self, width, height, players)
        for player in players:
            self.detect(player)
        
        if self.shooting:
            return self.shoot()
        else:
            return []
        
    def move(self, players):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def shoot(self, command = ""):
        return [Bullet(self.rect.center, self.facing, 10)]
        
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
            
            if not self.shooting:
                self.oldSpeedx = self.speedx
                self.oldSpeedy = self.speedy
                self.speedx = 0
                self.speedy = 0
            
            if math.fabs(pX-zX) > math.fabs(pY-zY):
                print "r/l"
                if pX > zX:
                    self.facing = "right"
                    self.shooting = True
                    
                else:
                    self.facing = "left"
                    self.shooting = True
            else:
                print "u/d"
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
          
          
