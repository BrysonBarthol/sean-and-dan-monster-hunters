import pygame, math, sys
from HUD import Text

class HUDAmmo(Text):
        def __init__(self, pos, baseText = "Ammo: ", textSize = 36, textColor=(255,255,255), font = None):
                self.ammo = 0
                self.baseText = baseText
                self.text = self.baseText + str(self.ammo)
                Text.__init__(self, pos, self.text, textSize, textColor, font)
                self.change = False
                        
        def setText(self, text):
                self.baseText = text
                self.change = True
                
        def update(self):
                if self.change:
                        self.text = self.baseText + str(self.ammo)
                        self.image = self.font.render(self.text, 1, self.textColor)
                        self.rect = self.image.get_rect(center = self.rect.center)
                        self.change = False
        
        def setAmmo(self, ammo):
                self.ammo = ammo
                self.change = True
                
        def increaseAmmo(self, amount = 1):
                self.ammo += amount
                self.change = True
        
        def decreaseAmmo(self, amount = (-1)):
                self.ammo += amount
                self.change = True
                
        def resetAmmo(self):
                self.ammo = 0
                self.change = True
