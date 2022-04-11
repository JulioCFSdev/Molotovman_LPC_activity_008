import pygame
from Brick import Bricks
from Config import screen, brick_coord, wall_coord, Constants 
from mobile_game_object import Draw_Players
from Bomb import Bomb
from Player import Soviet
bomb = Bomb()
x = 0


class Objects:
    class Draws:
        

        def collision_brick(self, explosion_list, duration_explosion):
            global wall_coord
            if duration_explosion > 0:
                for explosion in explosion_list:
                    for brick in wall_coord:
                        if pygame.Rect.colliderect(explosion, brick):
                            Constants.sound_hit.play()
                            del wall_coord[wall_coord.index(brick)]
                            brick_coord.remove(brick)
            return wall_coord



        def collision_player(self, explosion_list, player_rect, duration_explosion, player_type):

            death = False


            if duration_explosion > 0:
                for i in explosion_list:
                    if pygame.Rect.colliderect(i, player_rect):
                        Constants.sound_hit.play()
                        if player_type == "sve":
                            death = True
                        if player_type == "amr":
                            death = True
                return death
            else:

                return False


        def draw_arenabrk(self):
            global brick_coord
            for e in range(0, 1050, 50):
                screen.blit(Bricks.images(Bricks)[0], (e, 0))
                arenabrk_1 = pygame.Rect(e, 0, 50, 50)
                screen.blit(Bricks.images(Bricks)[0], (e, 700))
                arenabrk_2 = pygame.Rect(e, 700, 50, 50)
            for e in range(0, 800, 50):
                screen.blit(Bricks.images(Bricks)[0], (0, e))
                arenabrk_1 = pygame.Rect(0, e, 50, 50)
                screen.blit(Bricks.images(Bricks)[0], (900, e))
                arenabrk_2 = pygame.Rect(900, e, 50, 50)
            for i in range(0, 600, 100):
                for e in range(0, 700, 100):
                    screen.blit(Bricks.images(Bricks)[0], (150 + e, 100 + i))


        def draw_wallbrk(self):
            global brick_coord, wall_coord
            for i in range(0, 500, 100):
                for e in range(150, 800, 50):
                    wallbrk = pygame.Rect(e, 150 + i, 30, 30)
                    if wallbrk in wall_coord:
                        screen.blit(Bricks.images(Bricks)[1], (e, 150 + i))
            for i in range(0, 600, 100):
                for e in range(100, 650, 50):
                    wallbrk = pygame.Rect(200 + i, e, 30, 30)
                    if wallbrk in wall_coord:
                        screen.blit(Bricks.images(Bricks)[1], (200 + i, e))
            for i in range(0, 100, 50):
                for e in range(0, 150, 50):
                    wallbrk = pygame.Rect(50 + i, 320 + e, 30, 30)
                    if wallbrk in wall_coord:
                        screen.blit(Bricks.images(Bricks)[1], (50 + i, 320 + e))

                    wallbrk = pygame.Rect(800 + i, 320 + e, 30, 30)
                    if wallbrk in wall_coord:
                        screen.blit(Bricks.images(Bricks)[1], (800 + i, 320 + e))
            for i in range(0, 50, 50):
                for e in range(0, 150, 50):
                    wallbrk = pygame.Rect(450 + e, 650 + i, 30, 30)
                    if wallbrk in wall_coord:
                        screen.blit(Bricks.images(Bricks)[1], (450 + e, 650 + i))
                    wallbrk = pygame.Rect(450 + e, 50 + i, 30, 30)
                    if wallbrk in wall_coord:
                        screen.blit(Bricks.images(Bricks)[1], (450 + e, 50 + i))


        def draw_soviet_player(self):
            Draw_Players.draw_soviet(Draw_Players)

        def draw_american_player(self):
            Draw_Players.draw_american(Draw_Players)

        def draw_bomb(pos_x_s, pos_y_s, type_soldier):
            if type_soldier == 1:
                pos_init_x = pos_init_y = 50
            elif type_soldier == 2:
                pos_init_x = 850
                pos_init_y = 630
            screen.blit(bomb.img_dynamite, (pos_x_s + pos_init_x, pos_y_s + pos_init_y))
            

        def draw_explosion(pos_x_s, pos_y_s, type_soldier):
            if type_soldier == 1:
                pos_init_x = pos_init_y = 50
            elif type_soldier == 2:
                pos_init_x = 850
                pos_init_y = 630
            screen.blit(bomb.explosion_up, (pos_x_s + pos_init_x, pos_y_s + (pos_init_y - 50)))
            screen.blit(bomb.explosion_center, (pos_x_s + pos_init_x, pos_y_s + pos_init_y))
            screen.blit(bomb.explosion_left, (pos_x_s + (pos_init_x-50), pos_y_s + pos_init_y))
            screen.blit(bomb.explosion_right, (pos_x_s + (pos_init_x+50), pos_y_s + pos_init_y))
            screen.blit(bomb.explosion_down, (pos_x_s + pos_init_x, pos_y_s + (pos_init_y+50)))

        def colision_ply_brick(self, add_x, add_y, last_key_pressed):
            global x
            while x < len(brick_coord):
                if Draw_Players.draw_soviet(Soviet, add_x, add_y, last_key_pressed).colliderect(brick_coord[x]):
                    print("colidiu")
                x += 1