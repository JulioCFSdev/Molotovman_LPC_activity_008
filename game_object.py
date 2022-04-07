import pygame
from Brick import Bricks
from Config import screen



class Objects:
    class Draws:
        def draw_arenabrk(self):
            for e in range(0, 1100, 50):
                screen.blit(Bricks.images(Bricks)[0], (e, 0))
            for e in range(0, 1100, 50):
                screen.blit(Bricks.images(Bricks)[0], (e, 750))
            for e in range(0, 800, 50):
                screen.blit(Bricks.images(Bricks)[0], (0, e))
            for e in range(0, 800, 50):
                screen.blit(Bricks.images(Bricks)[0], (950, e))
            for i in range(20, 600, 100):
                for e in range(0, 800, 100):
                    screen.blit(Bricks.images(Bricks)[0], (150 + e, 100 + i))