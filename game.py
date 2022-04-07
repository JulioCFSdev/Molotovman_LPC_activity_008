import pygame
from Config import Constants, game_loop, screen,Colors
from main_screen import Main_screen

pygame.init()
pygame.display.set_caption("MolotovBoy - Cold War")


class Game:

    def game_loop():
        while game_loop:

            screen.fill(Colors.BLACK)
            Game.game_input()
            Game.game_process()
            Game.game_draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.time.Clock().tick(Constants.CLOCK_TICK)
            pygame.display.update()

            
    def game_input():
        pass


    def game_process():
        pass


    def game_draw():
        pass



Main_screen.menu()
Game.game_loop()