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
win = False

clock = pygame.time.Clock()

screenWidth = 1000 
screenHeight = 700

screenSize = screenWidth, screenHeight
screen = pygame.display.set_mode(screenSize)

bgColor = r,g,b = 0, 0, 0
level = Level("screen34", screenSize)
player = level.player

while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w or event.key == pygame.K_UP:
                                player.go("up")
                        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                                player.go("right")
                        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                                player.go("down")
                        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                                player.go("left")
                if event.type == pygame.KEYUP:
                        if event.key == pygame.K_w or event.key == pygame.K_UP:
                                player.go("stop up")
                        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                                player.go("stop right")
                        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                                player.go("stop down")
                        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                                player.go("stop left")


		if knife.living:
            knife.stab(player)


		#########----Player----##############
		player = Player(7, screenSize, [360, 510])
		#########-----HUD-----##############
		ammo = HUDAmmo
		coins = HUDCoins
		ammo = Score([400, 25], "Ammo: ", 36)
		coins = Score([600, 25], "Coins: ", 36)
		#########-----Background----##########

		red = 0
        green = 0
        blue = 0
        bgColor = red, green, blue
        screen.fill(bgColor)
        screen.blit(background.surface, background.rect)
        #########---Level-----##############
		screenCol, screenRow = 2,4
		screenMaxCol, screenMaxRow = 5, 7

		
#########-----Blocks----##########
		

#########-----HUD-----##########

################################
		pygame.display.flip()
