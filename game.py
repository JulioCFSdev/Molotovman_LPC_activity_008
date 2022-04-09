import pygame
from Config import Constants, game_loop, screen, Colors, background
from main_screen import Main_screen
from game_object import Objects
from mobile_game_object import Draw_Players
from Bomb import Bomb

pygame.init()
pygame.display.set_caption("MolotovBoy - Cold War")

add_xs = 0
add_ys = 0
add_xa = 0
add_ya = 0
bomb_ativation = False
last_key_pressed_s = 0
# Last_key_pressed_soviet = W -> 1
# Last_key_pressed_soviet = S -> 0
# Last_key_pressed_soviet = A -> 2
# Last_key_pressed_soviet = D -> 3

class Game:

    def __init__(self):
        self.cooldown_bomb = 0


    def game_input(self):
        global add_xs, add_ys, add_xa, add_ya, bomb_ativation, pos_bomb, last_key_pressed_s
        if pygame.key.get_pressed()[pygame.K_w]:
            add_ys -= 20
            last_key_pressed_s = 1
        if pygame.key.get_pressed()[pygame.K_s]:
            add_ys += 20
            last_key_pressed_s = 0
        if pygame.key.get_pressed()[pygame.K_a]:
            add_xs -= 20
            last_key_pressed_s = 2
        if pygame.key.get_pressed()[pygame.K_d]:
            add_xs += 20
            last_key_pressed_s = 3
        if pygame.key.get_pressed()[pygame.K_e]:
            bomb_ativation = True
            if last_key_pressed_s == 0:
                pos_bomb = [add_xs, add_ys + 50]
            elif last_key_pressed_s == 1:
                pos_bomb = [add_xs, add_ys - 50]
            elif last_key_pressed_s == 2:
                pos_bomb = [add_xs - 50, add_ys]
            elif last_key_pressed_s == 3:
                pos_bomb = [add_xs + 50, add_ys]
            self.cooldown_bomb = Constants.COOLDOWN_BOMB
            Bomb().create_bomb(add_xs, add_ys)
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
        Draw_Players.draw_soviet(Draw_Players, add_xs, add_ys, last_key_pressed_s)
        Draw_Players.draw_american(Draw_Players, add_xa, add_ya)
        if bomb_ativation and self.cooldown_bomb != 0:
            Objects.Draws.draw_bomb(pos_bomb[0], pos_bomb[1])
            self.cooldown_bomb -= 1 



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
Game().game_loop()
