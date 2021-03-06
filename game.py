import pygame
from Config import (
    Constants,
    game_loop,
    screen,
    Colors,
    background,
    time_counter,
    time_text,
    brick_coord,
)
from Player import American
from main_screen import Main_screen
from game_object import Objects
from mobile_game_object import Draw_Players
from Bomb import Bomb
from HUD import Hud

pygame.init()
pygame.display.set_caption("MolotovBoy - Cold War")
pygame.time.set_timer(pygame.USEREVENT, 120)

add_xs = 0
add_ys = 0
add_xa = 0
add_ya = 0
player_1 = 1
player_2 = 2
pause = False
bomb_ativation_s = False
bomb_ativation_a = False
explosion_ativation_s = False
explosion_ativation_a = False
respawn_sv = False
respawn_am = False
cooldown_bomb_s = 0
cooldown_bomb_a = 0
scr_sv = 0
scr_am = 0
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
    cooldown_bomb_s = 0
    cooldown_bomb_a = 0
    time_game = time_counter
    time_text = time_text

    def __init__(self):
        pygame.mixer.music.load("sounds/Gameplay_theme.mp3")
        pygame.mixer.music.play(-1)
        self.bomb_duration_s = 0
        self.bomb_duration_a = 0
        self.explosion_duration_s = 0
        self.explosion_duration_a = 0

    def game_input(self):
        global add_xs, add_ys, add_xa, add_ya, bomb_ativation_s, bomb_ativation_a, pos_bomb_s, pos_bomb_a, last_key_pressed_s, last_key_pressed_a, list_Bomb_s, list_Bomb_a, cooldown_bomb_s, cooldown_bomb_a, brick_coord
        if pygame.key.get_pressed()[pygame.K_w]:
            add_ys -= 20
            last_key_pressed_s = 1
        elif pygame.key.get_pressed()[pygame.K_s]:
            add_ys += 20
            last_key_pressed_s = 0
        elif pygame.key.get_pressed()[pygame.K_a]:
            add_xs -= 20
            last_key_pressed_s = 2
        elif pygame.key.get_pressed()[pygame.K_d]:
            add_xs += 20
            last_key_pressed_s = 3
        if pygame.key.get_pressed()[pygame.K_e] and cooldown_bomb_s <= 0:
            cooldown_bomb_s = Constants.COOLDOWN_BOMB
            bomb_ativation_s = True
            if last_key_pressed_s == 0:
                pos_bomb_s = [add_xs, add_ys + 100]
            elif last_key_pressed_s == 1:
                pos_bomb_s = [add_xs, add_ys]
            elif last_key_pressed_s == 2:
                pos_bomb_s = [add_xs - 50, add_ys + 50]
            elif last_key_pressed_s == 3:
                pos_bomb_s = [add_xs + 50, add_ys + 50]

            pos_bomb_s[0] = (pos_bomb_s[0] // 50) * 50
            pos_bomb_s[1] = (pos_bomb_s[1] // 50) * 50

            self.bomb_duration_s = Constants.BOMB_DURATION
            self.explosion_duration_s = Constants.EXPLOSION_DURATION
            list_Bomb_s = Bomb().create_bomb(add_xs, add_ys, player_1)
        if pygame.key.get_pressed()[pygame.K_UP]:
            add_ya -= 20
            last_key_pressed_a = 1
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            add_ya += 20
            last_key_pressed_a = 0
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            add_xa += 20
            last_key_pressed_a = 2
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            add_xa -= 20
            last_key_pressed_a = 3
        if pygame.key.get_pressed()[pygame.K_KP0] and cooldown_bomb_a <= 0:
            cooldown_bomb_a = Constants.COOLDOWN_BOMB
            bomb_ativation_a = True
            if last_key_pressed_a == 0:
                pos_bomb_a = [add_xa, add_ya + 100]
            elif last_key_pressed_a == 1:
                pos_bomb_a = [add_xa, add_ya]
            elif last_key_pressed_a == 2:
                pos_bomb_a = [add_xa + 50, add_ya + 50]
            elif last_key_pressed_a == 3:
                pos_bomb_a = [add_xa - 50, add_ya + 50]

            pos_bomb_a[0] = (pos_bomb_a[0] // 50) * 50
            pos_bomb_a[1] = (pos_bomb_a[1] // 50) * 50

            self.bomb_duration_a = Constants.BOMB_DURATION
            self.explosion_duration_a = Constants.EXPLOSION_DURATION
            list_Bomb_a = Bomb().create_bomb(add_xa, add_ya, player_2)

    def game_process(self):
        global time_game, time_text, soviet_rect, american_rect
        soviet_rect = Draw_Players().create_soviet(
            add_xs, add_ys, last_key_pressed_s
        )
        american_rect = Draw_Players().create_american(
            add_xa, add_ya, last_key_pressed_a
        )
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                time_game -= 1
                time_text = (
                    str(time_game).rjust(3) if time_game > 0 else "Times Over"
                )
            if time_text == "Times Over":
                game_over_text = Constants.PYFONT.render(
                    "GAME OVER", True, Colors.BLACK
                )
                screen.blit(
                    game_over_text,
                    (
                        Constants.SCREEN_SIZE[0] / 2 - 100,
                        Constants.SCREEN_SIZE[1] / 2,
                    ),
                )

    def wall_limits_soviet(self):
        global add_xs, add_ys, last_key_pressed_s

        if (
            Draw_Players.draw_soviet(
                Draw_Players, add_xs, add_ys, last_key_pressed_s
            )
            is True
        ):
            if last_key_pressed_s == 0:
                add_ys -= 25
            if last_key_pressed_s == 3:
                add_xs -= 25
            if last_key_pressed_s == 1:
                add_ys += 25
            if last_key_pressed_s == 2:
                add_xs += 35

    def wall_limits_american(self):
        global add_xa, add_ya, last_key_pressed_a

        if (
            Draw_Players.draw_american(
                Draw_Players, add_xa, add_ya, last_key_pressed_a
            )
            is True
        ):

            if last_key_pressed_a == 0:
                add_ya -= 25
            if last_key_pressed_a == 2:
                add_xa -= 25
            if last_key_pressed_a == 1:
                add_ya += 25
            if last_key_pressed_a == 3:
                add_xa += 35

    def game_draw(self):
        global explosion_range_s, explosion_range_a, explosion_ativation_s, explosion_ativation_a, cooldown_bomb_s, cooldown_bomb_a, add_xs, add_ys, add_xa, add_ya, scr_sv, scr_am, pause, respawn_sv, respawn_am
        screen.blit(background, (0, 0))
        Objects.Draws().draw_arenabrk()
        Objects.Draws().draw_wallbrk()
        if pause:
            pause_screen = pygame.image.load("img/Pause_screen.png")
            screen.blit(pause_screen, (262, 200))
            Hud.draw(Hud, str(scr_sv), str(scr_am))
            Draw_Players.draw_soviet(
                Draw_Players, add_xs, add_ys, last_key_pressed_s
            )
            Draw_Players.draw_american(
                Draw_Players, add_xa, add_ya, last_key_pressed_a
            )
            pygame.display.update()

        Draw_Players.draw_soviet(
            Draw_Players, add_xs, add_ys, last_key_pressed_s
        )
        Draw_Players.draw_american(
            Draw_Players, add_xa, add_ya, last_key_pressed_a
        )
        Hud.draw(Hud, str(scr_sv), str(scr_am))
        screen.blit(
            Constants.PYFONT.render(time_text, True, Colors.WHITE), (440, 745)
        )

        # Draw bomb and create rects to explosion range of soviet bomb
        if bomb_ativation_s and self.bomb_duration_s != 0:
            Objects.Draws.draw_bomb(pos_bomb_s[0], pos_bomb_s[1], player_1)
            self.bomb_duration_s -= 1
            cooldown_bomb_s -= 1
            if self.bomb_duration_s == 0:
                explosion_ativation_s = True
                explosion_range_s = Bomb().create_explosion(
                    pos_bomb_s[0], pos_bomb_s[1], player_1
                )
                # Sound explosion soviet
                Constants.sound_explosion.play()

        # Draw explosion range of soviet bomb
        if explosion_ativation_s and self.explosion_duration_s != 0:
            Objects.Draws().collision_brick(
                explosion_range_s, self.explosion_duration_s
            )
            Objects.Draws().collision_player(
                explosion_range_s,
                soviet_rect,
                self.explosion_duration_s,
                "sve",
            )
            Objects.Draws().collision_player(
                explosion_range_s,
                american_rect,
                self.explosion_duration_s,
                "amr",
            )
            Objects.Draws.draw_explosion(
                pos_bomb_s[0], pos_bomb_s[1], player_1
            )

            self.explosion_duration_s -= 1
            cooldown_bomb_s -= 1
            if self.explosion_duration_s == 0:
                explosion_ativation_s = False

            if add_xs == add_ys == 0 and scr_am >= 1:
                respawn_sv = True

            if add_xa == add_ya == 0 and scr_sv >= 1:
                respawn_am = True

            if (
                Objects.Draws().collision_player(
                    explosion_range_s,
                    soviet_rect,
                    self.explosion_duration_s,
                    "sve",
                )
                is True
                and respawn_sv is False
            ):
                add_xs = 0
                add_ys = 0
                add_xa = 0
                add_ya = 0
                scr_am += 1

            if (
                Objects.Draws().collision_player(
                    explosion_range_s,
                    american_rect,
                    self.explosion_duration_s,
                    "amr",
                )
                is True
                and respawn_am is False
            ):
                add_xs = 0
                add_ys = 0
                add_xa = 0
                add_ya = 0
                scr_sv += 1

            if scr_sv >= 3:
                win_screen = pygame.image.load("img/Player_1_win.png")
                Hud.draw(Hud, str(scr_sv), str(scr_am))
                screen.blit(win_screen, (200, 100))
                pygame.display.update()
                pygame.time.wait(3000)
                exit()

            if scr_am >= 3:
                win_screen = pygame.image.load("img/Player_2_win.png")
                Hud.draw(Hud, str(scr_sv), str(scr_am))
                screen.blit(win_screen, (200, 100))
                pygame.display.update()
                pygame.time.wait(3000)
                exit()

        # Draw bomb and create rects to explosion range of american bomb
        if bomb_ativation_a and self.bomb_duration_a != 0:
            Objects.Draws.draw_bomb(pos_bomb_a[0], pos_bomb_a[1], player_2)
            self.bomb_duration_a -= 1
            cooldown_bomb_a -= 1
            if self.bomb_duration_a == 0:
                explosion_ativation_a = True
                explosion_range_a = Bomb().create_explosion(
                    pos_bomb_a[0], pos_bomb_a[1], player_2
                )
                # Sound explosion american
                Constants.sound_explosion.play()

        # Draw explosion range of american bomb
        if explosion_ativation_a and self.explosion_duration_a != 0:
            Objects.Draws().collision_brick(
                explosion_range_a, self.explosion_duration_a
            )
            Objects.Draws().collision_player(
                explosion_range_a,
                american_rect,
                self.explosion_duration_a,
                "amr",
            )
            Objects.Draws().collision_player(
                explosion_range_a,
                soviet_rect,
                self.explosion_duration_a,
                "sve",
            )
            Objects.Draws.draw_explosion(
                pos_bomb_a[0], pos_bomb_a[1], player_2
            )

            self.explosion_duration_a -= 1
            cooldown_bomb_a -= 1
            if self.explosion_duration_a == 0:
                explosion_ativation_a = False

            if add_xs == add_ys == 0 and scr_am >= 1:
                respawn_sv = True

            if add_xa == add_ya == 0 and scr_sv >= 1:
                respawn_am = True

            if (
                Objects.Draws().collision_player(
                    explosion_range_a,
                    american_rect,
                    self.explosion_duration_a,
                    "amr",
                )
                is True
                and respawn_am is False
            ):
                add_xs = 0
                add_ys = 0
                add_xa = 0
                add_ya = 0
                scr_sv += 1

            if (
                Objects.Draws().collision_player(
                    explosion_range_a,
                    soviet_rect,
                    self.explosion_duration_a,
                    "sve",
                )
                is True
                and respawn_sv is False
            ):
                add_xs = 0
                add_ys = 0
                add_xa = 0
                add_ya = 0
                scr_am += 1

            if scr_sv == 3:
                win_screen = pygame.image.load("img/Player_1_win.png")
                Hud.draw(Hud, str(scr_sv), str(scr_am))
                screen.blit(win_screen, (200, 100))
                pygame.display.update()
                pygame.time.wait(3000)
                exit()

            if scr_am == 3:
                win_screen = pygame.image.load("img/Player_2_win.png")
                Hud.draw(Hud, str(scr_sv), str(scr_am))
                screen.blit(win_screen, (200, 100))
                pygame.display.update()
                pygame.time.wait(3000)
                exit()

        respawn_am = False
        respawn_sv = False

    def game_loop(self):
        global pause
        while game_loop:

            if pause:
                Game.game_draw(Game)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            pause = not pause
                continue

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
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pause = not pause

            pygame.display.flip()
            pygame.time.Clock().tick(Constants.CLOCK_TICK)


Main_screen.menu()
Game().game_loop()
