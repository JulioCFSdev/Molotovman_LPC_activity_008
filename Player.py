import pygame
from Config import screen

pygame.init()

class Soviet:

    def __init__(self,velocity):
        self.velocity = velocity
        self.soviet_soldier = pygame.image.load("sprites\Player\Player_1_front.png")
        screen.blit(self.soviet_soldier,(50,50))


class American:
    def __init__(self, velocity):
        self.velocity = velocity
        self.american_soldier = pygame.image.load("sprites\Player\Player_1_front.png")
        screen.blit(self.american_soldier, (850, 650))


