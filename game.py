import pygame
from Config import Constants, game_loop, screen, Colors, background, time_counter, time_text
from main_screen import Main_screen
from game_object import Objects
from mobile_game_object import Draw_Players
from Bomb import Bomb

pygame.init()
pygame.display.set_caption("MolotovBoy - Cold War")
pygame.time.set_timer(pygame.USEREVENT, 120)

add_xs = 0
add_ys = 0
add_xa = 0
add_ya = 0
bomb_ativation = False
explosion_ativation = False
cooldown_bomb = 0
# Last_key_pressed_soviet = W -> 1
# Last_key_pressed_soviet = S -> 0
# Last_key_pressed_soviet = A -> 2
# Last_key_pressed_soviet = D -> 3
last_key_pressed_s = 0
# Last_key_pressed_american = up -> 1
# Last_key_pressed_american = down -> 0
# Last_key_pressed_american = left -> 2
# Last_key_pressed_american = right -> 3
last_key_pressed_a = 0


class Game:
    global time_game, time_text
    cooldown_bomb = 0
    time_game = time_counter
    time_text = time_text
    def __init__(self):
        self.bomb_duration = 0
        self.explosion_duration = 0


    def game_input(self):
        global add_xs, add_ys, add_xa, add_ya, bomb_ativation, pos_bomb, last_key_pressed_s, last_key_pressed_a, list_Bomb, cooldown_bomb
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
        if pygame.key.get_pressed()[pygame.K_e] and cooldown_bomb <= 0:
            cooldown_bomb = Constants.COOLDOWN_BOMB
            bomb_ativation = True
            if last_key_pressed_s == 0:
                pos_bomb = [add_xs, add_ys + 50]
            elif last_key_pressed_s == 1:
                pos_bomb = [add_xs, add_ys]
            elif last_key_pressed_s == 2:
                pos_bomb = [add_xs - 50, add_ys + 50]
            elif last_key_pressed_s == 3:
                pos_bomb = [add_xs + 50, add_ys + 50]

            pos_bomb[0] = (pos_bomb[0]//50) * 50
            pos_bomb[1] = (pos_bomb[1]//50) * 50

            self.bomb_duration = Constants.BOMB_DURATION
            self.explosion_duration = Constants.EXPLOSION_DURATION
            list_Bomb = Bomb().create_bomb(add_xs, add_ys)
        if pygame.key.get_pressed()[pygame.K_UP]:
            add_ya -= 20
            last_key_pressed_a = 1
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            add_ya += 20
            last_key_pressed_a = 0
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            add_xa += 20
            last_key_pressed_a = 2
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            add_xa -= 20
            last_key_pressed_a = 3


    def game_process(self):
        global time_game, time_text
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                time_game -= 1
                time_text = str(time_game).rjust(3) if time_game > 0 else 'Times Over'
            if time_text == 'Times Over':
                game_over_text = Constants.PYFONT.render("GAME OVER", True, Colors.BLACK)
                screen.blit(game_over_text, (Constants.SCREEN_SIZE[0] / 2 - 100, Constants.SCREEN_SIZE[1] / 2))

    def wall_limits_soviet(self):
        global add_xs, add_ys

        if add_xs < 0:
            add_xs = 0

        if add_xs >= 800:
            add_xs = 800

        if add_ys >= 570:
            add_ys = 570

        if add_ys <= 0:
            add_ys = 0

    def wall_limits_american(self):
        global add_xa, add_ya

        if add_ya >= 0:
            add_ya = 0

        if add_ya <= -595:
            add_ya = -595

        if add_xa >= 0:
            add_xa = 0

        if add_xa <= -800:
            add_xa = -800





    def game_draw(self):
        global explosion_range, explosion_ativation, cooldown_bomb
        screen.blit(background, (0, 0))
        Objects.Draws().draw_arenabrk()
        Objects.Draws().draw_wallbrk()
        Draw_Players.draw_soviet(Draw_Players, add_xs, add_ys, last_key_pressed_s)
        Draw_Players.draw_american(Draw_Players, add_xa, add_ya, last_key_pressed_a)
        screen.blit(Constants.PYFONT.render(time_text, True, Colors.BLACK), (Constants.SCREEN_SIZE[0] / 2, 5))
        if bomb_ativation and self.bomb_duration != 0:
            Objects.Draws.draw_bomb(pos_bomb[0], pos_bomb[1])
            self.bomb_duration -= 1
            cooldown_bomb -= 1
            if self.bomb_duration == 0:
                explosion_ativation = True
                explosion_range = Bomb().create_explosion(add_xs, add_ys)

        if explosion_ativation and self.explosion_duration != 0:
            Objects.Draws.draw_explosion(pos_bomb[0], pos_bomb[1])
            self.explosion_duration -= 1
            cooldown_bomb -= 1
            if self.explosion_duration == 0:
                explosion_ativation = False

    def game_loop(self):
        while game_loop:

            screen.fill(Colors.BLACK)
            Game.game_input(Game)
            Game.game_process(Game)
            Game.game_draw(Game)
            Game.wall_limits_soviet(Game)
            Game.wall_limits_american(Game)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            
            pygame.display.flip()
            pygame.time.Clock().tick(Constants.CLOCK_TICK)

Main_screen.menu()
Game().game_loop()
