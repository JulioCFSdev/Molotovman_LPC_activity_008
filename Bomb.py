import pygame
from Config import screen
from mobile_game_object import Draw_Players


class Bomb:
    def __init__(self):
        self.img_dynamite = pygame.image.load("sprites/Dynamite_normal.png")


    def create_bomb(self, pos_x_s, pos_y_s):
        bomb = pygame.Rect(pos_x_s + 50, pos_y_s + 100, 45, 45)
