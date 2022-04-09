import pygame

from Config import screen
from Player import Soviet, American

pygame.init()

class Draw_Players:

    def draw_soviet(self, add_x, add_y, last_key_pressed):
        pos_x_s = 50 + add_x
        pos_y_s = 50 + add_y
        screen.blit(Soviet.soviet_soldier(Soviet, last_key_pressed),(pos_x_s, pos_y_s))

    def draw_american(self, add_x, add_y, last_key_pressed):
        pos_x_a = 850 + add_x
        pos_y_a = 630 + add_y
        screen.blit(American.american_soldier(American, last_key_pressed),(pos_x_a, pos_y_a))
