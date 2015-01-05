import pygame, math
from Block import Block
#from Deamon import Deamon
#from Ghost import Ghost
#from Leviathan import Leviathan
from Level import Level
#from HUDAmmo import HUDAmmo
#from HUDCoin import HUDCoins
#from HUDHeart import HUDHearts
from LevelChangeBlock import LevelChangeBlock

pygame.init()
win = False

clock = pygame.time.Clock()

screenWidth = 1000 
screenHeight = 700

screenSize = screenWidth, screenHeight
screen = pygame.display.set_mode(screenSize)

bgColor = r,g,b = 0, 0, 0
level = Level("screen24", ["Dan", "Sean"], screenSize)
players = level.players

#ammo = HUDAmmo
#coins = HUDCoins
#ammo = Score([400, 25], "Ammo: ", 36)
#coins = Score([600, 25], "Coins: ", 36)

while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w or event.key == pygame.K_UP:
                                players[0].go("up")
                        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                                players[0].go("right")
                        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                                players[0].go("down")
                        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                                players[0].go("left")
                if event.type == pygame.KEYUP:
                        if event.key == pygame.K_w or event.key == pygame.K_UP:
                                players[0].go("stop up")
                        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                                players[0].go("stop right")
                        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                                players[0].go("stop down")
                        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                                players[0].go("stop left")
        
        for player in players:
            player.update(screenWidth, screenHeight)
            
        for block in level.hardBlocks:
            for player in players:
                if block.playerCollide(player):
                    player.go("stop")
        for levelChangeBlock in level.levelChangeBlocks:
            for player in players:
                if block.playerCollide(player):
                    print "new level"
                    level.load(newlev)
                    

        red = 0
        green = 0
        blue = 0
        bgColor = red, green, blue
        screen.fill(bgColor)
        for block in level.blocks:
            screen.blit(block.image, block.rect)
        for levelChangeBlock in level.levelChangeBlocks:
            screen.blit(levelChangeBlock.image, levelChangeBlock.rect)
        for player in players:
            screen.blit(player.image, player.rect)
        pygame.display.flip()
