import random

import pygame


class PowerUp(pygame.sprite.Sprite):

    def __init__(self, window, x, y, player):
        pygame.sprite.Sprite.__init__(self)
        self.x = random.randint(0, 1280)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 40, 40)
        self.color = (0, 255, 0)
        self.velX = random.randint(0, 1280)
        self.velY = 8
        self.speedmod = 10
        self.win = window
        self.onwindow = True
        self.player = player

    def draw(self):
        pygame.draw.rect(self.win, self.color, self.rect)

    def movement(self):
        if self.onwindow:
            self.y += 3
            self.rect = pygame.Rect(int(self.x), int(self.y), 5, 5)

            if self.x >= 1280 or self.y >= 960:
                self.x = random.randint(0, 1280)
                self.y = 0




    def PowerUpPLay(self):
        self.movement()
        self.draw()

    def killSelf(self):
        self.onwindow = False
        self.x = 0
        self.y = 0
        self.color = (0, 0, 0)
        self.rect = pygame.Rect(int(self.x), int(self.y), 5, 5)
        self.kill()

    def reset(self):
        self.x = random.randint(0, 1280)
        self.y = 0
        self.color = (0, 255, 0)
        self.onwindow = True
        self.rect = pygame.Rect(int(self.x), int(self.y), 5, 5)








