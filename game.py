import pygame

import Player
from Config import Constants, game_loop, screen, Colors, background
from main_screen import Main_screen
from game_object import Objects
from Player import Soviet, American
from mobile_game_object import Draw_Players

pygame.init()
pygame.display.set_caption("MolotovBoy - Cold War")

add_x = 0
add_y = 0

class Game:

    def game_input(self):
        global add_x, add_y
        if pygame.key.get_pressed()[pygame.K_w]:
            add_y -= 10
        if pygame.key.get_pressed()[pygame.K_s]:
            add_y += 10
        if pygame.key.get_pressed()[pygame.K_a]:
            add_x -= 10
        if pygame.key.get_pressed()[pygame.K_d]:
            add_x += 10


    def game_process(self):
        pass

    def game_draw(self):
        screen.blit(background, (0, 0))
        Objects.Draws.draw_arenabrk(Objects.Draws)
        Objects.Draws.draw_wallbrk(Objects.Draws)
        Draw_Players.draw_soviet(Draw_Players, add_x, add_y)
        Objects.Draws.draw_american_player(Objects.Draws)


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
