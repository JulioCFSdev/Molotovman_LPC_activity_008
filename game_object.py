import pygame
from Brick import Bricks
from Config import screen, brick_coord
from mobile_game_object import Draw_Players
from Bomb import Bomb
from Player import Soviet
bomb = Bomb()
x = 0


class Objects:
    class Draws:
        
        def draw_arenabrk(self):
            global brick_coord
            for e in range(0, 1050, 50):
                screen.blit(Bricks.images(Bricks)[0], (e, 0))
                arenabrk = pygame.Rect(e, 0, 50, 50)
            for e in range(0, 1050, 50):
                screen.blit(Bricks.images(Bricks)[0], (e, 700))
                arenabrk = pygame.Rect(e, 700, 50, 50)
            for e in range(0, 800, 50):
                screen.blit(Bricks.images(Bricks)[0], (0, e))
                arenabrk = pygame.Rect(0, e, 50, 50)
            for e in range(0, 800, 50):
                screen.blit(Bricks.images(Bricks)[0], (900, e))
                arenabrk = pygame.Rect(900, e, 50, 50)
            for i in range(0, 600, 100):
                for e in range(0, 700, 100):
                    screen.blit(Bricks.images(Bricks)[0], (150 + e, 100 + i))


        def draw_wallbrk(self):
            global brick_coord
            for i in range(0, 500, 100):
                for e in range(150, 800, 50):
                    screen.blit(Bricks.images(Bricks)[1], (e, 150 + i))
                    wallbrk = pygame.Rect(e, 150 + i, 50, 50)
            for i in range(0, 600, 100):
                for e in range(100, 650, 50):
                    screen.blit(Bricks.images(Bricks)[1], (200 + i, e))
                    wallbrk = pygame.Rect(200 + i, e, 50, 50)
            for i in range(0, 100, 50):
                for e in range(0, 150, 50):
                    screen.blit(Bricks.images(Bricks)[1], (50 + i, 320 + e))
                    wallbrk = pygame.Rect(50 + i, 320 + e, 50, 50)
            for i in range(0, 100, 50):
                for e in range(0, 150, 50):
                    wallbrk = pygame.Rect(800 + i, 320 + e, 50, 50)
                    screen.blit(Bricks.images(Bricks)[1], (800 + i, 320 + e))
            for i in range(0, 50, 50):
                for e in range(0, 150, 50):
                    screen.blit(Bricks.images(Bricks)[1], (450 + e, 650 + i))
                    wallbrk = pygame.Rect(450 + e, 650 + i, 50, 50)
            for i in range(0, 50, 50):
                for e in range(0, 150, 50):
                    screen.blit(Bricks.images(Bricks)[1], (450 + e, 50 + i))
                    wallbrk = pygame.Rect(450 + e, 650 + i, 50, 50)

        def draw_soviet_player(self):
            Draw_Players.draw_soviet(Draw_Players)

        def draw_american_player(self):
            Draw_Players.draw_american(Draw_Players)

        def draw_bomb(pos_x_s, pos_y_s):
            screen.blit(bomb.img_dynamite, (pos_x_s + 50, pos_y_s + 50))

        def draw_exploding_bomb(pos_x_s, pos_y_s):
            screen.blit(bomb.img_dynamite_exploding,(pos_x_s + 50, pos_y_s + 50))

        def draw_explosion(pos_x_s, pos_y_s):
            screen.blit(bomb.explosion_up, (pos_x_s + 50, pos_y_s))
            screen.blit(bomb.explosion_center, (pos_x_s + 50, pos_y_s + 50))
            screen.blit(bomb.explosion_left, (pos_x_s, pos_y_s + 50))
            screen.blit(bomb.explosion_right, (pos_x_s + 100, pos_y_s + 50))
            screen.blit(bomb.explosion_down, (pos_x_s + 50, pos_y_s + 100))

        def colision_ply_brick(self, add_x, add_y, last_key_pressed):
            global x
            while x < len(brick_coord):
                if Draw_Players.draw_soviet(Soviet, add_x, add_y, last_key_pressed).colliderect(brick_coord[x]):
                    print("colidiu")
                x += 1