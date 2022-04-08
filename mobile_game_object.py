import pygame

from Config import screen
from Player import Soviet, American

pygame.init()

class Draw_Players:

    def draw_soviet(self, add_x, add_y):
        screen.blit(Soviet.soviet_soldier(Soviet),(50 + add_x, 50 + add_y))

    def draw_american(self):
        screen.blit(American.american_soldier(American),(850, 650))
