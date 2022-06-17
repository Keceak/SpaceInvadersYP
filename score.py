import pygame.font
from gun import Gun
from pygame.sprite import Group

class Score(): # вывод счета

    def __init__(self, screen, stats): #инициализируем подсчет очков
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (21, 255, 0)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_best_score()
        self.image_guns()

    def image_score(self): #переводит текст счета в изображение
        self.score_image = self.font.render(str(self.stats.score), True, self.text_color, (0, 0 , 0))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 6
        self.score_rect.top = 10

    def image_best_score(self): #преобразует рекорд в изображение
        self.best_score_image = self.font.render(str(self.stats.best_score), True, self.text_color, (0, 0, 0))
        self.best_score_rect = self.best_score_image.get_rect()
        self.best_score_rect.centerx = self.screen_rect.centerx
        self.best_score_rect.top = self.screen_rect.top + 10

    def image_guns(self): # кол-во попыток
        self.guns = Group()
        for gun_number in range(self.stats.guns_left):
            gun = Gun(self.screen)
            gun.rect.x = 10 + gun_number * gun.rect.width
            gun.rect.y = 10
            self.guns.add (gun)

    def show_score(self): #вывод счета на экран
        self.screen.blit(self.score_image, self.score_rect) #отрисовка на экране
        self.screen.blit(self.best_score_image, self.best_score_rect)
        self.guns.draw(self.screen)

