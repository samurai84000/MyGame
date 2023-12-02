import pygame.sprite


class Laserbeam(pygame.sprite.Sprite):
    def __init__(self, col=(255, 0, 0), x=0, y=0, width=5, height=10, damage=1):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.damage = damage
        self.col = col

    def update(self, x, y):
        self.rect.move_ip(x, y)

        if self.rect.bottom <= 0:
            self.kill()

    def getcolor(self):
        return self.col

    def getdamage(self):
        return self.damage

    def explode(self):
        self.update(0, 0)
        self.col = (255, 0, 0)
        self.damage = 10




