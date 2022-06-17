import pygame

class Enemy(pygame.sprite.Sprite): # чтобы можно было объединить в 1 группу и будут делать одни и теже действия(класс 1 пришельца)

    def __init__(self, screen): #задаем начальную позицию
        super(Enemy, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Graph/pixil-frame-0 (11).png') # подгрузка изображения
        self.rect = self.image.get_rect() # преобразования изображения в прямоугольник
        self.rect.x = self.rect.width # отрисовка координат х
        self.rect.y = self.rect.height # отрисовка координат y
        self.x = float(self.rect.x) # перевод rect в вещественное число чтобы объекты двигались плавнее
        self.x = float(self.rect.y)

    def draw(self): # вывод енеми на экран
        self.screen.blit(self.image, self.rect)

    def update(self): # перемещает противников на экране
        self.y += 0.03
        self.rect.y = self.y
