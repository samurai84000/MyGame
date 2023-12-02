import pygame
from BombAttack import BombAttack

from Laserbeam import Laserbeam
from MiniEnemy import MiniEnemy

class Boss:
    def __init__(self, x, y, window, window_width, window_height):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 100, 100)
        self.color = (50, 50, 50)
        self.speed = 2
        self.health = 2000

        self.window = window
        self.window_width = window_width
        self.window_heigh = window_height

        self.helperships = pygame.sprite.Group()

        self.moveleft = False

        self.laserbeams = pygame.sprite.Group()
        self.fastlaserbeams = pygame.sprite.Group()
        self.bombs = pygame.sprite.Group()
        self.MiniEnemys = pygame.sprite.Group()

        self.framecounter = 0
        self.attackcounter = 0
        self.cyclecounter = 0
        self.bombframes = 0

        self.helpership = self.createhelpership(142, -50)
        self.helpership2 = self.createhelpership(862, -50)

        self.MiniEnemy1 = MiniEnemy(1250, 100, 40, 40, 10, window)
        self.MiniEnemys.add(self.MiniEnemy1)



    def draw(self):
        if self.health >= 0:
            pygame.draw.rect(self.window, self.color, self.rect)
        else:
            pygame.draw.rect(self.window, (255, 0, 0), self.rect)



        if len(self.laserbeams) != 0:
            for i in self.laserbeams:
                pygame.draw.rect(self.window, i.getcolor(), i)
        if len(self.fastlaserbeams) != 0:
            for i in self.fastlaserbeams:
                pygame.draw.rect(self.window, i.getcolor(), i)
        if len(self.bombs) != 0:
            for i in self.bombs:
                pygame.draw.rect(self.window, i.getcolor(), i.getRect())
        if len(self.MiniEnemys) != 0:
            for i in self.MiniEnemys:
                i.draw()







    def movement(self):
        if self.framecounter >= 60 and self.attackcounter < 20:
            self.helpership.y = -50
            self.helpership2.y = -50
            self.attack()
            self.framecounter = -1

        if 20 <= self.attackcounter <= 25:
            pygame.draw.rect(self.window, (255, 255, 255), self.helpership)
            pygame.draw.rect(self.window, (255, 255, 255), self.helpership2)
            if self.framecounter >= 60:
                self.helpership.y = self.helpership.y + 20
                self.helpership2.y = self.helpership2.y + 20
                self.attack()
                self.framecounter = -1



        if self.attackcounter > 25:
            pygame.draw.rect(self.window, (255,255,255), self.helpership)
            pygame.draw.rect(self.window, (255, 255, 255), self.helpership2)
            if self.framecounter >= 300:
                self.attack()
                self.framecounter = -1
            if self.framecounter % 5 == 0:
                self.attacklaser()
        self.framecounter += 1

        if self.moveleft:
            self.x -= self.speed
        else:
            self.x += self.speed

        if self.rect.left <= self.window_width / 5:
            self.x = self.window_width / 5 + 1
            self.moveleft = False

        if self.rect.right >= self.window_width / 5 * 4:
            self.x = (self.window_width / 5 * 4) - 101
            self.moveleft = True
        self.rect = pygame.Rect(int(self.x), int(self.y), 100, 100)

    def bossDoesTheThing(self):

        for i in self.laserbeams:
            i.update(0, 2)
        for i in self.fastlaserbeams:
            i.update(0, 5)
        for i in self.bombs:
            i.update(0, 2)
        for i in self.MiniEnemys:
            i.update(2, 0)

        self.draw()
        self.movement()

    def attack(self):
        if self.attackcounter < 10:
            laser = Laserbeam((255, 0, 0), self.rect.bottom + self.x, self.rect.y + self.rect.y, 5, 10, 1)
            bomb = BombAttack((255, 0, 0), self.rect.x, self.rect.y, 20, 20, 10)
            self.bombs.add(bomb)
            self.laserbeams.add(laser)
            self.attackcounter += 1
        elif self.attackcounter >= 10 and self. attackcounter <= 20:
            laser = Laserbeam((128, 0, 180), self.rect.bottom + self.x, self.rect.y + self.rect.y, 50, 100, 3)
            self.laserbeams.add(laser)
            self.attackcounter += 1
        else:
            self.attackcounter += 1



    def attacklaser(self):
        if 25 <= self.attackcounter <= 200:
            laser = Laserbeam((255, 0, 0), self.rect.bottom + 180, self.rect.y + 150, 50, 100, 3)
            laser1 = Laserbeam((255, 0, 0), self.rect.bottom + 900, self.rect.y + 150, 50, 100, 3)

            self.fastlaserbeams.add(laser)
            self.fastlaserbeams.add(laser1)
            self.attackcounter += 1

        elif self.attackcounter > 200:
            self.resetMiniEnemy()
            self.attackcounter = 0

        else:
            self.attackcounter += 1
            
    def createhelpership(self, x, y):
        return pygame.Rect(self.rect.bottom + x, self.rect.y + y, 75, 100)

    def resetMiniEnemy(self):
        temp = pygame.sprite.Group()
        t = MiniEnemy(1250, 100, 40, 40, 10, self.window)
        temp.add(t)
        self.MiniEnemys = temp










