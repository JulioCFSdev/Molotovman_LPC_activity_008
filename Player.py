import pygame


pygame.init()

class Soviet:

    def soviet_soldier(self, last_key_pressed):
        if last_key_pressed == 0:
            soviet_soldier = pygame.image.load("sprites/Player/Player_red_front.png")
        elif last_key_pressed == 1:
            soviet_soldier = pygame.image.load("sprites/Player/Player_red_front.png")
        elif last_key_pressed == 2:
            soviet_soldier = pygame.image.load("sprites/Player/Player_red_left.png")
        elif last_key_pressed == 3:
            soviet_soldier = pygame.image.load("sprites/Player/Player_red_right.png")
        return (soviet_soldier)


class American:
    def american_soldier(self):
        american_soldier_up = pygame.image.load("sprites/Player/Player_1_front.png")
        american_soldier_down = pygame.image.load("sprites/Player/Player_1_front.png")
        american_soldier_left = pygame.image.load("sprites/Player/Player_1_front.png")
        american_soldier_right = pygame.image.load("sprites/Player/Player_1_front.png")
        
        return (american_soldier_up)


