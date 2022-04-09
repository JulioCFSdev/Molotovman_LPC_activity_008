import pygame


pygame.init()

class Soviet:

    def soviet_soldier(self):
        soviet_soldier = pygame.image.load("sprites/Player/Player_red_front.png")
        return (soviet_soldier)


class American:
    def american_soldier(self):
        american_soldier = pygame.image.load("sprites/Player/Player_usa_front.png")
        return (american_soldier)


