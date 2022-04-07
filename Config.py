import pygame


pygame.init()

class Colors:
    BLACK = (0, 0, 0)
    GREEN = (10, 189, 31)
    WHITE = (255, 255, 255)
    BLUE = (0, 110, 230)
    BROWN = (137, 50, 3)
    YELLOW = (255, 195, 0)

class Constants:
    FONT = "img/upheavtt.ttf"
    CLOCK_TICK = 60
    SCREEN_SIZE = (1000, 800)

game_loop = True
screen = pygame.display.set_mode(Constants.SCREEN_SIZE)
background = pygame.image.load("sprites/Backgound.png")