import math

import Laserbeam
import pygame, sys

from Boss import Boss
from Player import Player
from PowerUp import PowerUp

# Constants
WIDTH, HEIGHT = 1280, 850
TITLE = "Smooth Movement"

# pygame initialization
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
backround = pygame.image.load("pixel-1280x960.png").convert()
bg = backround.get_rect()

bg_height = backround.get_height()
scroll = 0
pixel_count = 0

tiles = math.ceil(HEIGHT / bg_height)

clock = pygame.time.Clock()

# Player Initialization
player = Player(WIDTH / 2, HEIGHT / 2, win, WIDTH, HEIGHT)
boss = Boss(WIDTH / 2, 0, win, WIDTH, HEIGHT)
powerup = PowerUp(win, 0, 0, player)

counter = 0


def interact():
    if pygame.Rect.colliderect(player.rect, powerup.rect):
        player.laserPowerUpLevel += 1
        powerup.killSelf()

    if len(player.laserbeams) != 0:
        for i in player.laserbeams:
            if pygame.Rect.colliderect(boss.rect, i):
                boss.health -= i.getdamage()
                i.kill()
    if len(boss.fastlaserbeams) != 0:
        for i in boss.fastlaserbeams:
            if pygame.Rect.colliderect(player.rect, i):
                player.health = player.health - i.getdamage()
                i.kill()

    if len(boss.laserbeams) != 0:
        for i in boss.laserbeams:
            if pygame.Rect.colliderect(player.rect, i):
                player.health -= i.getdamage()
                i.kill()
    if len(boss.bombs) != 0:
        for i in boss.bombs:
            if pygame.Rect.colliderect(player.rect, i):
                player.health -= i.getdamage()
                i.kill()
    if len(boss.MiniEnemy1.getBombs()) != 0:
        for i in boss.MiniEnemy1.getBombs():
            if pygame.Rect.colliderect(player.rect, i):
                player.health -= i.getdamage()
                i.kill()

    if player.health <= 0:
        player.disabled = False


# Main Loop
while True:
    win.blit(backround, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True
            if event.key == pygame.K_SPACE:
                player.spacebar_press = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False
            if event.key == pygame.K_SPACE:
                player.spacebar_press = False

    # Draw

    interact()
    powerup.PowerUpPLay()
    player.playerDoesTheThings()
    boss.bossDoesTheThing()
    pygame.display.update()
    pygame.display.flip()


    if powerup.onwindow == False and counter >= 1000:
        powerup.reset()
        counter = 0

    counter += 1
    clock.tick(120)
