import pygame


class Bomb:
    def __init__(self):
        self.img_dynamite = pygame.image.load("sprites/Explosion/Dynamite_normal.png")
        self.img_dynamite_exploding = pygame.image.load("sprites/Explosion/Dynamite_exploding.png")
        self.explosion_up = pygame.image.load("sprites/Explosion/explosion_corner_up.png")
        self.explosion_center = pygame.image.load("sprites/Explosion/explosion_center.png")
        self.explosion_left = pygame.image.load("sprites/Explosion/explosion_corner_left.png")
        self.explosion_right = pygame.image.load("sprites/Explosion/explosion_corner_right.png")
        self.explosion_down = pygame.image.load("sprites/Explosion/explosion_corner_down.png")

    def create_bomb(self, pos_x_s, pos_y_s, type_soldier):
        if type_soldier == 1:
            pos_init_x = pos_init_y = 50
        elif type_soldier == 2:
            pos_init_x = 850
            pos_init_y = 630

        bomb = pygame.Rect(pos_x_s + pos_init_x, pos_y_s + pos_init_y, 45, 45)

        return bomb

    def exploding_bomb(self, pos_x_s, pos_y_s, type_soldier):
        if type_soldier == 1:
            pos_init_x = pos_init_y = 50
        elif type_soldier == 2:
            pos_init_x = 850
            pos_init_y = 630
        
        explosion = pygame.Rect(pos_x_s + pos_init_x, pos_y_s + pos_init_y, 45, 45)

        return explosion

    def create_explosion(self, pos_x_s, pos_y_s, type_soldier):
        if type_soldier == 1:
            pos_init_x = 50
            pos_init_y = 50

        elif type_soldier == 2:
            pos_init_x = 850
            pos_init_y = 630

        explosion_up = pygame.Rect(pos_x_s + pos_init_x, pos_y_s + (pos_init_y - 50), 45, 45)
        explosion_center = pygame.Rect(pos_x_s + pos_init_x, pos_y_s + pos_init_y, 45, 45)
        explosion_left = pygame.Rect(pos_x_s + (pos_init_x-50), pos_y_s + pos_init_y, 45, 45)
        explosion_right = pygame.Rect(pos_x_s + (pos_init_x+50), pos_y_s + pos_init_y, 45, 45)
        explosion_down = pygame.Rect(pos_x_s + pos_init_x, pos_y_s + (pos_init_y+50), 45, 45)
            

        return [explosion_up, explosion_center, explosion_left, explosion_right, explosion_down]
