import pygame, math, sys, os
from Block import Block
from Demon import Demon
from Ghost import Ghost
from Leviathan import Leviathan
from Level import Level
from LevelChangeBlock import LevelChangeBlock
from Bullet import Bullet
from MainMenu import Button
from HUDHeart import HUDHearts
from Pestilence import Pestilence
pygame.init()
win = False

clock = pygame.time.Clock()

bullets = []

screenWidth = 1000 
screenHeight = 700

screenSize = screenWidth, screenHeight
screen = pygame.display.set_mode(screenSize)

bgImage = pygame.image.load("RSC/MainMenu/Title Screen.png").convert()
bgRect = bgImage.get_rect()

bgColor = r,g,b = 0, 0, 0
level = Level("screen24", ["Dan", "Sean"], screenSize)
players = level.players
ghosts = level.ghosts
leviathans = level.leviathans
demons = level.demons
pestilences = level.pestilences

playButton = Button([screenWidth/2, screenHeight-300], 
                                     "RSC/MainMenu/playbutton.png", 
                                     "RSC/MainMenu/playbuttonpressed.png")

run = False
#ammo = HUDAmmo
#coins = HUDCoins
#ammo = Score([400, 25], "Ammo: ", 36)
#coins = Score([600, 25], "Coins: ", 36)

pygame.mixer.music.load("RSC/Audio/Music/bgm_action_1.mp3")
pygame.mixer.music.play(-1, 0.0)
bgImage = pygame.image.load("RSC/MainMenu/Title Screen.png").convert()
bgRect = bgImage.get_rect()

HUDs = []

while True:
    while not run:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT: sys.exit()
                    if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                    run = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                            playButton.click(event.pos)
                    if event.type == pygame.MOUSEBUTTONUP:
                            if playButton.release(event.pos):
                                    run = True
            bgColor = r,g,b
            screen.fill(bgColor)
            screen.blit(bgImage, bgRect)
            screen.blit(playButton.image, playButton.rect)
            pygame.display.flip()
            clock.tick(60)
            
            
    pygame.mixer.music.load("RSC/Audio/Music/bgm_action_1.mp3")
    pygame.mixer.music.play(-1, 0.0) 
    HUDs += [HUDHearts([screenWidth-60, 10],players[0])]  
            
    while run and players[0].living:
        for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    level.killOldLevels(0)
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w or event.key == pygame.K_UP:
                                players[0].go("up")
                        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                                players[0].go("right")
                        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                                players[0].go("down")
                        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                                players[0].go("left")
                        if event.key == pygame.K_SPACE:
                                bullets += player.shoot()
                if event.type == pygame.KEYUP:
                        if event.key == pygame.K_w or event.key == pygame.K_UP:
                                players[0].go("stop up")
                        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                                players[0].go("stop right")
                        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                                players[0].go("stop down")
                        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                                players[0].go("stop left")
                        if event.key == pygame.K_SPACE:
                                player.shoot("stop")
        
            
        
        
        for player in players:
            player.update(screenWidth, screenHeight)
            
        for ghost in ghosts:
            ghost.update(screenWidth, screenHeight)
        
        for leviathan in leviathans:
            leviathan.update(screenWidth, screenHeight, players)
        
        for demon in demons:
            demon.update(screenWidth, screenHeight, players)
        
        for pestilence in pestilences:
            pestilence.update(screenWidth, screenHeight, players)
        
        for hud in HUDs:
            hud.update()    
            
        for ghost in ghosts:
            for player in players:
                player.collideMonster(ghost)
                
        for leviathan in leviathans:
            for player in players:
                player.collideMonster(leviathan)
                
        for demon in demons:
            for player in players:
                player.collideMonster(demon)
                
        for pestilence in pestilences:
            for player in players:
                player.collideMonster(pestilence)
            
        for block in level.hardBlocks:
            for player in players:
                if block.playerCollide(player):
                    player.go("stop")
            for demon in demons:
                if block.demonCollide(demon):
                    demon.speedx = -demon.speedx
                    demon.speedy = -demon.speedy
            for leviathan in leviathans:
                if block.leviathanCollide(leviathan):
                    leviathan.speedx = -leviathan.speedx
                    leviathan.speedy = -leviathan.speedy
            for pestilence in pestilences:
                if block.pestilenceCollide(pestilence):
                    pestilence.speedx = -pestilence.speedx
                    pestilence.speedy = -pestilence.speedy
        for levelChangeBlock in level.levelChangeBlocks:
            #print levelChangeBlock.newlev
            for player in players:
                if levelChangeBlock.playerCollide(player):
                    print "new level"
                    level.load(levelChangeBlock.newlev, levelChangeBlock.kind)
            for demon in demons:
                if levelChangeBlock.demonCollide(demon):
                    demon.speedx = -demon.speedx
                    demon.speedy = -demon.speedy
            for leviathan in leviathans:
                if levelChangeBlock.leviathanCollide(leviathan):
                    leviathan.speedx = -leviathan.speedx
                    leviathan.speedy = -leviathan.speedy
            for pestilence in pestilences:
                if levelChangeBlock.pestilenceCollide(pestilence):
                    pestilence.speedx = -pestilence.speedx
                    pestilence.speedy = -pestilence.speedy
        for bullet in bullets:
            bullet.update(screenWidth, screenHeight)
            for block in level.hardBlocks:
                bullet.collideBlock(block)
            for enemy in level.ghosts:
                bullet.collideCreature(enemy)
                enemy.collideBullet(bullet)
            for enemy in level.demons:
                bullet.collideCreature(enemy)
                enemy.collideBullet(bullet)
            for enemy in level.leviathans:
                bullet.collideCreature(enemy)
                enemy.collideBullet(bullet)
            for enemy in level.pestilences:
                bullet.collideCreature(enemy)
                enemy.collideBullet(bullet)
                
        
        #print len(bullets)        
        for bullet in bullets:
            if not bullet.living:
                bullets.remove(bullet)
        for enemy in level.ghosts:
            if not enemy.living:
                level.ghosts.remove(enemy)

        for enemy in level.leviathans:
            if not enemy.living:
                level.leviathans.remove(enemy)

        for enemy in level.demons:
            if not enemy.living:
                level.demons.remove(enemy)
                
        for enemy in level.pestilences:
            if not enemy.living:
                level.pestilences.remove(enemy)

                
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
        for bullet in bullets:
            screen.blit(bullet.image, bullet.rect)
        for ghost in ghosts:
            screen.blit(ghost.image, ghost.rect)
        for demon in demons:
            screen.blit(demon.image, demon.rect)
        for leviathan in leviathans:
            screen.blit(leviathan.image, leviathan.rect)
        for hud in HUDs:
            screen.blit(hud.image, hud.rect)
        for pestilence in pestilences:
            screen.blit(pestilence.image, pestilence.rect)
        pygame.display.flip()
        
    bgImage = pygame.image.load("RSC/MainMenu/gameover.png").convert()
    bgRect = bgImage.get_rect()
    
    while run and not players[0].living:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                playButton.click(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if playButton.release(event.pos):
                    run = True
                    level.killOldLevels(0)
                    level = Level("screen24", ["Dan", "Sean"], screenSize)
                    players = level.players
                    ghosts = level.ghosts
                    leviathans = level.leviathans
                    demons = level.demons
                    pestilences = level.pestilences
                    
        bgColor = r,g,b
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        screen.blit(playButton.image, playButton.rect)
        pygame.display.flip()
        clock.tick(60)
