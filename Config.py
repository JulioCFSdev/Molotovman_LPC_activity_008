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
    PYFONT = pygame.font.Font(FONT, 50)
    CLOCK_TICK = 60
    SCREEN_SIZE = (950, 750)
    BOMB_DURATION = 20
    EXPLOSION_DURATION = 7
    COOLDOWN_BOMB = BOMB_DURATION + EXPLOSION_DURATION

game_loop = True
screen = pygame.display.set_mode(Constants.SCREEN_SIZE)
background = pygame.image.load("sprites/Scenario/Background.png")
time_text = '180'.rjust(3)
time_counter = 180