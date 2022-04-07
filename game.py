import pygame
from Config import Constants, game_loop, screen,Colors
from main_screen import Main_screen
from game_object import Objects

pygame.init()
pygame.display.set_caption("MolotovBoy - Cold War")


class Game:

    def game_input(self):
        pass

    def game_process(self):
        pass

    def game_draw(self):
        Objects.Draws.draw_arenabrk(Objects.Draws)

    def game_loop(self):
        while game_loop:

            screen.fill(Colors.BLACK)
            Game.game_input(Game)
            Game.game_process(Game)
            Game.game_draw(Game)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.time.Clock().tick(Constants.CLOCK_TICK)
            pygame.display.update()

            




Main_screen.menu()
Game.game_loop(Game)