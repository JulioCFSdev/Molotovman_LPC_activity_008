import pygame

from Config import screen, brick_coord
from Player import Soviet, American

pygame.init()

class Draw_Players:

    def draw_soviet(self, add_x, add_y, last_key_pressed):
        pos_x_s = 50 + add_x
        pos_y_s = 50 + add_y
        screen.blit(Soviet.soviet_soldier(Soviet, last_key_pressed),(pos_x_s, pos_y_s))
        obj_soviet = Soviet.soviet_soldier(Soviet, last_key_pressed).get_rect(center=(pos_x_s, pos_y_s))
        if pygame.Rect.collidelist(obj_soviet, brick_coord):
            print((obj_soviet.x, obj_soviet.y))
            print("colidiu")


        return obj_soviet

    def draw_american(self, add_x, add_y, last_key_pressed):
        pos_x_a = 850 + add_x
        pos_y_a = 630 + add_y
        screen.blit(American.american_soldier(American, last_key_pressed),(pos_x_a, pos_y_a))

