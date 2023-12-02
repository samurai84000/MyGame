# Player Class
import pygame

from  Laserbeam import Laserbeam

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, window, window_width, window_height):
        pygame.sprite.Sprite.__init__(self)
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.spacebar_press = False
        self.speed = 4
        self.disabled = True

        self.window = window
        self.window_width = window_width
        self.window_heigh = window_height

        self.laserbeams = pygame.sprite.Group()
        self.laserPowerUpLevel = 0

        self.health = 3

    def draw(self):
        if self.rect.right >= self.window_width:
            self.x = self.window_width - 32
            self.rect.right = self.window_width
        elif self.rect.left <= 0:
            self.x = 0
            self.rect.left = 0

        if self.rect.top <= 0:
            self.y = 0
            self.rect.topleft = (self.x, 0)
        elif self.rect.bottom >= self.window_heigh:
            self.y = self.window_heigh - 32
            self.rect.bottom = self.window_heigh

        if self.health > 0:
            pygame.draw.rect(self.window, self.color, self.rect)
        else:
            pygame.draw.rect(self.window, (255, 0, 0), self.rect)

        if len(self.laserbeams) != 0:
            for laser in self.laserbeams:
                pygame.draw.rect(self.window, laser.getcolor(), laser)


    def update(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed
        if self.spacebar_press:

            if self.laserPowerUpLevel == 0:
                laser = Laserbeam((255, 0, 0), self.x + 11, self.y - 11, 5, 10, 1)
                self.laserbeams.add(laser)
            elif self.laserPowerUpLevel == 1:
                laser1 = Laserbeam((255, 0, 0), self.x + 7, self.y - 27, 5, 10, 1)
                laser2 =  Laserbeam((255, 0, 0), self.x + 27, self.y - 5, 5, 10, 1)
                self.laserbeams.add(laser1)
                self.laserbeams.add(laser2)
            elif self.laserPowerUpLevel == 2:
                laser = Laserbeam((0, 255, 0), self.x, self.rect.y, 5, 10, 1)
                laser1 = Laserbeam((0, 255, 0), self.x + 16, self.rect.y, 5, 10, 1)
                laser2 = Laserbeam((0, 255, 0), self.x + 32, self.rect.y, 5, 10, 1)
                self.laserbeams.add(laser1)
                self.laserbeams.add(laser2)
                self.laserbeams.add(laser)
            else:
                laser = Laserbeam((255, 0, 0), self.x + 11, self.y - 7, 50, 100, 4)
                self.laserbeams.add(laser)

        for i in self.laserbeams:
            i.update(0, -32)
        self.x += self.velX
        self.y += self.velY

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)

    def playerDoesTheThings(self):
        if(self.disabled):
            self.draw()
            self.update()
