import pygame, math
from Block import Block
from Deamon import Deamon
from Ghost import Ghost
from Leviathan import Leviathan
from Level import Level

pygame.init()

clock = pygame.time.Clock()

width = 1000 
height = 700
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)

screenCol, screenRow = 2,4
screenMaxCol, screenMaxRow = 5, 7

level = Level("screen"+ str(screenCol) + str(screenRow))
