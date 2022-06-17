import pygame
from pygame.sprite import Sprite


class Gun(Sprite):

    def __init__(self, screen): #инициализация пушки
        super (Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Graph/pixil-frame-0 (6).png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.toright = False
        self.toleft = False

    def output(self):
        # Рисование пушки
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        # обновление позиции пушки
        if self.toright and self.rect.right < self.screen_rect.right:
            self.center += 0.72
        if self.toleft and self.rect.left > 0:
            self.center -= 0.75

        self.rect.centerx = self.center

    def create_gun(self): #размешает оружие по центру снизу
        self.center = self.screen_rect.centerx













