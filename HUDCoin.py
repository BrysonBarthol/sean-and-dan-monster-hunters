import pygame, math, sys

class HUDCoins(Text):
        def __init__(self, pos, baseText = "Coins: ", textSize = 36, textColor=(255,255,255), font = None):
                self.coins = 0
                self.baseText = baseText
                self.text = self.baseText + str(self.coins)
                Text.__init__(self, pos, self.text, textSize, textColor, font)
                self.change = False
                        
        def setText(self, text):
                self.baseText = text
                self.change = True
                
        def update(self):
                if self.change:
                        self.text = self.baseText + str(self.coins)
                        self.image = self.font.render(self.text, 1, self.textColor)
                        self.rect = self.image.get_rect(center = self.rect.center)
                        self.change = False
        
        def setCoins(self, coins):
                self.coins = coins
                self.change = True
                
        def increaseCoins(self, amount = 1):
                self.coins += amount
                self.change = True
                
        def resetCoins(self):
                self.coins = 0
                self.change = True
