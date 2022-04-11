import pygame

pygame.init()


class Soviet:
    def soviet_soldier(self, last_key_pressed):
        if last_key_pressed == 0:
            soviet_soldier = pygame.image.load(
                "sprites/Player/Player_red_front.png"
            )
        elif last_key_pressed == 1:
            soviet_soldier = pygame.image.load(
                "sprites/Player/Player_red_back.png"
            )
        elif last_key_pressed == 2:
            soviet_soldier = pygame.image.load(
                "sprites/Player/Player_red_left.png"
            )
        elif last_key_pressed == 3:
            soviet_soldier = pygame.image.load(
                "sprites/Player/Player_red_right.png"
            )

        return soviet_soldier


class American:
    def american_soldier(self, last_key_pressed):
        if last_key_pressed == 0:
            american_soldier = pygame.image.load(
                "sprites/Player/Player_usa_front.png"
            )
        elif last_key_pressed == 1:
            american_soldier = pygame.image.load(
                "sprites/Player/Player_usa_back.png"
            )
        elif last_key_pressed == 2:
            american_soldier = pygame.image.load(
                "sprites/Player/Player_usa_right.png"
            )
        elif last_key_pressed == 3:
            american_soldier = pygame.image.load(
                "sprites/Player/Player_usa_left.png"
            )

        return american_soldier
