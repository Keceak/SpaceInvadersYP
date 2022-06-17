import pygame
import movement
import pygame_menu

from gun import Gun
from pygame.sprite import Group
from stats import Stats
from score import Score





def run():

    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    pygame.display.set_caption("Space Invaders")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    enemys = Group()
    movement.create_army(screen, enemys)
    stats = Stats()
    score = Score(screen, stats)





    while True:

                movement.events(screen, gun, bullets)
                if stats.run_game:
                    gun.update_gun()
                    movement.update(bg_color, screen, stats, score, gun, enemys,  bullets)
                    movement.update_bullets(screen, stats, score, enemys, bullets)
                    movement.update_enemys(stats, screen, score, gun, enemys, bullets)


run()



