import pygame, math
from Block import Block
from Deamon import Deamon
from Ghost import Ghost
from Leviathan import Leviathan
from Level import Level
from HUDAmmo import HUDAmmo
from HUDCoin import HUDCoins
from HUDHeart import HUDHearts

pygame.init()

clock = pygame.time.Clock()

width = 1000 
height = 700
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)


#########-----HUD-----##############
ammo = HUDAmmo
coins = HUDCoins
ammo = Score([400, 25], "Ammo: ", 36)
coins = Score([600, 25], "Coins: ", 36)
#####################################


screenCol, screenRow = 2,4
screenMaxCol, screenMaxRow = 5, 7

level = Level("screen"+ str(screenCol) + str(screenRow))

#########-----HUD-----##########
screen.blit(ammo.image, ammo.rect)
screen.blit(coins.image, coins.rect)
################################
