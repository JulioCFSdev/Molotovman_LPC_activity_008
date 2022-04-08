import pygame
from Brick import Bricks
from Config import screen
from mobile_game_object import Draw_Players
from Bomb import Bomb



class Objects:
    class Draws:
        def draw_arenabrk(self):
            for e in range(0, 1050, 50):
                screen.blit(Bricks.images(Bricks)[0], (e, 0))
            for e in range(0, 1050, 50):
                screen.blit(Bricks.images(Bricks)[0], (e, 700))
            for e in range(0, 800, 50):
                screen.blit(Bricks.images(Bricks)[0], (0, e))
            for e in range(0, 800, 50):
                screen.blit(Bricks.images(Bricks)[0], (900, e))
            for i in range(0, 600, 100):
                for e in range(0, 700, 100):
                    screen.blit(Bricks.images(Bricks)[0], (150 + e, 100 + i))

        def draw_wallbrk(self):
            for i in range(0, 500, 100):
                for e in range(150, 800, 50):
                    screen.blit(Bricks.images(Bricks)[1], (e, 150 + i))
            for i in range(0, 600, 100):
                for e in range(100, 650, 50):
                    screen.blit(Bricks.images(Bricks)[1], (200 + i, e))
            for i in range(0, 100, 50):
                for e in range(0, 150, 50):
                    screen.blit(Bricks.images(Bricks)[1], (50 + i, 320 + e))
            for i in range(0, 100, 50):
                for e in range(0, 150, 50):
                    screen.blit(Bricks.images(Bricks)[1], (800 + i, 320 + e))
            for i in range(0, 50, 50):
                for e in range(0, 150, 50):
                    screen.blit(Bricks.images(Bricks)[1], (450 + e, 650 + i))
            for i in range(0, 50, 50):
                for e in range(0, 150, 50):
                    screen.blit(Bricks.images(Bricks)[1], (450 + e, 50 + i))

        def draw_soviet_player(self):
            Draw_Players.draw_soviet(Draw_Players)

        def draw_american_player(self):
            Draw_Players.draw_american(Draw_Players)

        def draw_bomb( pos_x_s, pos_y_s):
            screen.blit(Bomb().img_dynamite, (pos_x_s + 100, pos_y_s + 100))
