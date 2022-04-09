import pygame
from Config import Constants, game_loop, screen, Colors, background
from main_screen import Main_screen
from game_object import Objects
from mobile_game_object import Draw_Players

pygame.init()
pygame.display.set_caption("MolotovBoy - Cold War")

add_xs = 0
add_ys = 0
add_xa = 0
add_ya = 0

class Game:

    def game_input(self):
        global add_xs, add_ys, add_xa, add_ya
        if pygame.key.get_pressed()[pygame.K_w]:
            add_ys -= 20
            
        if pygame.key.get_pressed()[pygame.K_s]:
            add_ys += 20
        if pygame.key.get_pressed()[pygame.K_a]:
            add_xs -= 20
        if pygame.key.get_pressed()[pygame.K_d]:
            add_xs += 20
        if pygame.key.get_pressed()[pygame.K_UP]:
            add_ya -= 20
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            add_ya += 20
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            add_xa += 20
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            add_xa -= 20


    def game_process(self):
        pass

    def game_draw(self):
        screen.blit(background, (0, 0))
        Objects.Draws.draw_arenabrk(Objects.Draws)
        Objects.Draws.draw_wallbrk(Objects.Draws)
        Draw_Players.draw_soviet(Draw_Players, add_xs, add_ys)
        Draw_Players.draw_american(Draw_Players, add_xa, add_ya)


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
