import pygame
import sys
import time

from bullet import Bullet
from enemy import Enemy


def events(screen, gun, bullets):
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #вправо
            if event.key == pygame.K_d:
                gun.toright = True
            elif event.key == pygame.K_a:
                gun.toleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            #вправо
            if event.key == pygame.K_d:
                gun.toright = False
            elif event.key == pygame.K_a:
                gun.toleft = False

def update(bg_color,screen, stats, score, gun, enemys, bullets):
    # Обновление экрана
    screen.fill(bg_color)
    score.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    enemys.draw(screen)
    pygame.display.flip()

def update_bullets(screen, stats, score, enemys, bullets):
    #Обновлять позиции пулек
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, enemys, True, True)# перебираем группы пришельцев и пуль и если образутеся коллизия , то добавляем в словарь
                                                                        # аргументы Тру показывают что надо будет удалять и пулю и врага
    if collisions:
        for enemys in collisions.values():
            stats.score += 1 * len(enemys)
        score.image_score()
        check_best_score(stats, score)
        score.image_guns()

    if len(enemys) == 0:
        bullets.empty()
        create_army(screen, enemys)


def gun_kill(stats, screen, score, gun, enemys, bullets): # столкновение пушки и противника
    if stats.guns_left > 0: # если жизней больше 0, то делаем дальнейшие действия
        stats.guns_left -= 1
        score.image_guns()
        enemys.empty()
        bullets.empty()
        create_army(screen, enemys)
        gun.create_gun()
        time.sleep(1.5)
    else:
        stats.run_game = False
        sys.exit()

def update_enemys(stats, screen, score, gun, enemys, bullets): # обновляет позицию противников
    enemys.update()
    if pygame.sprite.spritecollideany(gun, enemys):
        gun_kill(stats, screen, score, gun, enemys, bullets)
    enemys_check(stats, screen, score, gun, enemys, bullets)

def enemys_check(stats, screen, score, gun, enemys, bullets): #проверка , пришельцы до конца
    screen_rect = screen.get_rect()
    for enemy in enemys.sprites():
        if enemy.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, score, gun, enemys, bullets)
            break

def create_army(screen, enemys): #создаем много противников
    enemy = Enemy(screen)
    enemy_width = enemy.rect.width
    number_enemy_x = int((600 - 2 * enemy_width) / enemy_width)
    enemy_height = enemy.rect.height
    number_enemy_y = int((800 - 300 - 2 * enemy_height) / enemy_height)


    for row_number in range (number_enemy_y):
         for enemy_number in range (number_enemy_x):
             enemy = Enemy(screen)
             enemy.x = enemy_width + enemy_width * enemy_number
             enemy.y = enemy_height + enemy_height * row_number
             enemy.rect.x = enemy.x
             enemy.rect.y = enemy.rect.height + enemy.rect.height * row_number
             enemys.add(enemy)

def check_best_score(stats, score): #проверка нового рекорда
    if stats.score > stats.best_score:
        stats.best_score = stats.score
        score.image_best_score() #проверяем рекорд постоянно так как он может появиться
        with open ('BestScore.txt', 'w') as f:
            f.write(str(stats.best_score))



