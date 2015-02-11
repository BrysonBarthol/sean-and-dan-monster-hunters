import pygame
from Creature import Creature
from Bullet import Bullet
from Knife import Knife

class Player(Creature):
    def __init__(self, guy, pos):
        Creature.__init__(self, "RSC/Player/DeanUp1.png", [0,0], pos, 9, 9)
        self.guy = guy
        if self.guy == "Dan":
            self.upImages = [pygame.image.load("RSC/Player/DeanUp1.png"),
                             pygame.image.load("RSC/Player/DeanUp2.png")]
            self.downImages = [pygame.image.load("RSC/Player/DeanDown1.png"),
                               pygame.image.load("RSC/Player/DeanDown2.png")]
            self.leftImages = [pygame.image.load("RSC/Player/DeanLeft1.png"),
                               pygame.image.load("RSC/Player/DeanLeft2.png")]
            self.rightImages = [pygame.image.load("RSC/Player/DeanRight1.png"),
                                pygame.image.load("RSC/Player/DeanRight2.png")]
            self.upKnifeImages = [pygame.image.load("RSC/Player/DeanUpKnife1.png"),
                             pygame.image.load("RSC/Player/DeanUpKnife2.png")]
            self.downKnifeImages = [pygame.image.load("RSC/Player/DeanDownKinfe1.png"),
                               pygame.image.load("RSC/Player/DeanDownKnife2.png")]
            self.leftKnifeImages = [pygame.image.load("RSC/Player/DeanLeftKnife1.png"),
                               pygame.image.load("RSC/Player/DeanLeftKnife2.png")]
            self.rightKnifeImages = [pygame.image.load("RSC/Player/DeanRightKnife1.png"),
                                pygame.image.load("RSC/Player/DeanRightKnife2.png")]
            self.upRangedImages = [pygame.image.load("RSC/Player/DeanUp1.png"),
                             pygame.image.load("RSC/Player/DeanUp2.png")]
            self.downRangedImages = [pygame.image.load("RSC/Player/DeanDown1.png"),
                               pygame.image.load("RSC/Player/DeanDown2.png")]
            self.leftRangedImages = [pygame.image.load("RSC/Player/DeanLeft1.png"),
                               pygame.image.load("RSC/Player/DeanLeft2.png")]
            self.rightRangedImages = [pygame.image.load("RSC/Player/DeanRight1.png"),
                                pygame.image.load("RSC/Player/DeanRight1.png")]
        else:
            self.upImages = [pygame.image.load("RSC/Player/SamUp1.png"),
                             pygame.image.load("RSC/Player/SamUp2.png")]
            self.downImages = [pygame.image.load("RSC/Player/SamDown1.png"),
                               pygame.image.load("RSC/Player/SamDown2.png")]
            self.leftImages = [pygame.image.load("RSC/Player/SamLeft1.png"),
                               pygame.image.load("RSC/Player/SamLeft2.png")]
            self.rightImages = [pygame.image.load("RSC/Player/SamRight1.png"),
                                pygame.image.load("RSC/Player/SamRight2.png")]
            self.upKnifeImages = [pygame.image.load("RSC/Player/SamUpKnife1.png"),
                             pygame.image.load("RSC/Player/SamUpKnife2.png")]
            self.downKnifeImages = [pygame.image.load("RSC/Player/SamDownKnife1.png"),
                               pygame.image.load("RSC/Player/SamDownKnife2.png")]
            self.leftKnifeImages = [pygame.image.load("RSC/Player/SamLeftKnife1.png"),
                               pygame.image.load("RSC/Player/SamLeftKnife2.png")]
            self.rightKnifeImages = [pygame.image.load("RSC/Player/SamRightKnife1.png"),
                                pygame.image.load("RSC/Player/SamRightKnife2.png")]
            self.upRangedImages = [pygame.image.load("RSC/Player/SamUp1.png"),
                             pygame.image.load("RSC/Player/SamUp2.png")]
            self.downRangedImages = [pygame.image.load("RSC/Player/SamDown1.png"),
                               pygame.image.load("RSC/Player/SamDown2.png")]
            self.leftRangedImages = [pygame.image.load("RSC/Player/SamLeft1.png"),
                               pygame.image.load("RSC/Player/SamLeft2.png")]
            self.rightRangedImages = [pygame.image.load("RSC/Player/SamRight1.png"),
                                pygame.image.load("RSC/Player/SamRight2.png")]
        self.facing = "up"
        self.changed = False
        self.images = self.upImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = self.rect.center)
        self.maxSpeed = 3
        self.shooting = False
        self.stabbing = False
        self.moving = False
        self.maxHurtDelay = 30 * 2
        self.hurtDelay = 0
        self.invincible = False
        
    #def stab(self):
     #   pass
        #return Knife(self.rect.center, self.facing) 0
      #  self.changed = True
      #  self.stabbing = True
    
    def shoot(self, command = ""):
        if command == "stop":
            self.shooting = False
        #if self.gun.coolDown == 0:
            #self.gun.coolDown += 1
        return [Bullet(self.rect.center, self.facing, 10)]
        
            
    def update(self, width, height):
        Creature.update(self, width, height)
        self.animate()
        self.changed = False
        if self.hurtDelay > 0:
            self.hurtDelay -= 1
        else:
            self.invincible = False
        
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
    
    def animate(self):
        if self.moving:
            if self.waitCount < self.maxWait:
                self.waitCount += 1
            else:
                self.waitCount = 0
                self.changed = True
                if self.frame < self.maxFrame:
                    self.frame += 1
                else:
                    self.frame = 0
                    if self.shooting:
                        self.shooting = False
                        self.images = self.upImages
                    if self.stabbing:
                        self.stabbing = False
                        self.images = self.upImages
        else:
            self.waitCount = self.maxWait
        
        if self.changed:    
            if self.facing == "up":
                if self.shooting:
                    self.images = self.upRangedImages
                elif self.stabbing:
                    self.images = self.upKnifeImages
                else:
                    self.images = self.upImages
            elif self.facing == "down":
                self.images = self.downImages
            elif self.facing == "right":
                self.images = self.rightImages
            elif self.facing == "left":
                self.images = self.leftImages
            
            self.image = self.images[self.frame]
    
    def collideMonster(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if (self.radius + other.radius) > self.distance(other.rect.center):
                    self.hurt()
    
    def hurt(self, amount=1):
        if not self.invincible:
            self.health -= amount
            self.invincible = True
            self.hurtDelay = self.maxHurtDelay
        
        if self.health <=0:
            self.living = False
            
    def go(self, direction):
        if direction == "up":
            self.facing = "up"
            self.changed = True
            self.speedy = -self.maxSpeed
            self.moving = True
        elif direction == "stop up":
            self.speedy = 0
            self.changed = True
            self.moving = False
        elif direction == "down":
            self.facing = "down"
            self.changed = True
            self.speedy = self.maxSpeed
            self.moving = True
        elif direction == "stop down":
            self.speedy = 0
            self.moving = False
            
        if direction == "right":
            self.facing = "right"
            self.changed = True
            self.speedx = self.maxSpeed
            self.moving = True
        elif direction == "stop right":
            self.speedx = 0
            self.moving = False
        elif direction == "left":
            self.facing = "left"
            self.changed = True
            self.speedx = -self.maxSpeed
            self.moving = True
        elif direction == "stop left":
            self.speedx = 0
            self.moving = False
        elif direction == "stop":
            print self.rect
            self.speedx = -self.speedx
            self.speedy = -self.speedy
            self.move()
            print self.rect
            self.speedx = 0
            self.speedy = 0
            self.moving = False
            
    
        
            
 




