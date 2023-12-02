import pygame
import pygame.sprite
from BombAttack import BombAttack

from  Laserbeam import Laserbeam


class MiniEnemy(pygame.sprite.Sprite):
    def __init__(self, x , y, width, height, health, window):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.color = (255, 0, 0)
        self.window_width = width
        self.window_height = height
        self.health = health
        self.window = window

        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.tracker = 0
        self.t = 0
        self.prev = 0

        self.framecounter = 0
        self.bombFrameCounter = 0

        self.bombs = pygame.sprite.Group()

    def getHealth(self):
        return self.health

    def update(self, x, y):
        for i in self.bombs:
            i.update(0, 0)
        if self.framecounter >= 2:
            self.tracker = self.tracker + x
            self.t = self.prev - round((4 / 490) * (self.tracker - 280) ** 2 - 640)
            self.prev = round((4 / 490) * (self.tracker - 280) ** 2 - 640)
            self.rect.move_ip(-self.t, x)
            self.framecounter = 0
        self.framecounter+=1

        if self.bombFrameCounter >= 80:
            self.dropBombs()
            self.bombFrameCounter = 0
        self.bombFrameCounter+=1

    def draw(self):
        if self.health >= 0:
            pygame.draw.rect(self.window, self.color, self.rect)
        if len(self.bombs) != 0:
            for i in self.bombs:
                pygame.draw.rect(self.window, i.getcolor(), i.getRect())


    def getcolor(self):
        return self.color

    def getRect(self):
        return self.rect

    def dropBombs(self):
        bomb = BombAttack((255, 0, 0), self.rect.x, self.rect.y, 20, 20, 10)
        self.bombs.add(bomb)

    def getBombs(self):
        return self.bombs



