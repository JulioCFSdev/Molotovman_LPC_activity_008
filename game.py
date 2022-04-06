import pygame
from Config import Constants, game_loop, screen,Colors

pygame.init()
pygame.display.set_caption("MolotovBoy - Cold War")


class Game:

    while game_loop:

        screen.fill(Colors.BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
