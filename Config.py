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
    SCREEN_SIZE = (950, 800)
    BOMB_DURATION = 20
    EXPLOSION_DURATION = 7
    COOLDOWN_BOMB = BOMB_DURATION + EXPLOSION_DURATION

game_loop = True
screen = pygame.display.set_mode(Constants.SCREEN_SIZE)
background = pygame.image.load("sprites/Scenario/Background.png")
Hud = pygame.image.load("sprites/Scenario/HUD.png")
time_text = '180'.rjust(3)
time_counter = 180
brick_coord = []
brick_list = []
wall_coord = []

for e in range(0, 1050, 50):
    arenabrk = pygame.Rect(e, 0, 30, 30)
    if arenabrk not in brick_coord:
        brick_coord.append(arenabrk)
for e in range(0, 1050, 50):
    arenabrk = pygame.Rect(e, 700, 30, 30)
    if arenabrk not in brick_coord:
        brick_coord.append(arenabrk)
for e in range(0, 800, 50):
    arenabrk = pygame.Rect(0, e, 30, 30)
    if arenabrk not in brick_coord:
        brick_coord.append(arenabrk)
for e in range(0, 800, 50):
    arenabrk = pygame.Rect(900, e, 30, 30)
    if arenabrk not in brick_coord:
        brick_coord.append(arenabrk)
for i in range(0, 600, 100):
    for e in range(0, 700, 100):
        arenabrk = pygame.Rect(150 + e, 100 + i, 30, 30)
        if arenabrk not in brick_coord:
            brick_coord.append(arenabrk)

for i in range(0, 500, 100):
    for e in range(150, 800, 50):
        wallbrk = pygame.Rect(e, 150 + i, 30, 30)
        if wallbrk not in brick_coord:
            brick_coord.append(wallbrk)
        if wallbrk not in wall_coord:
            wall_coord.append(wallbrk)
for i in range(0, 600, 100):
    for e in range(100, 650, 50):
        wallbrk = pygame.Rect(200 + i, e, 30, 30)
        if wallbrk not in brick_coord:
            brick_coord.append(wallbrk)
        if wallbrk not in wall_coord:
            wall_coord.append(wallbrk)
for i in range(0, 100, 50):
     for e in range(0, 150, 50):
        wallbrk = pygame.Rect(50 + i, 320 + e, 30, 30)
        if wallbrk not in brick_coord:
            brick_coord.append(wallbrk)
        if wallbrk not in wall_coord:
            wall_coord.append(wallbrk)
for i in range(0, 100, 50):
     for e in range(0, 150, 50):
        wallbrk = pygame.Rect(800 + i, 320 + e, 30, 30)
        if wallbrk not in brick_coord:
            brick_coord.append(wallbrk)
        if wallbrk not in wall_coord:
            wall_coord.append(wallbrk)
for i in range(0, 50, 50):
    for e in range(0, 150, 50):
        wallbrk = pygame.Rect(450 + e, 650 + i, 30, 30)
        if wallbrk not in brick_coord:
            brick_coord.append(wallbrk)
        if wallbrk not in wall_coord:
            wall_coord.append(wallbrk)
for i in range(0, 50, 50):
    for e in range(0, 150, 50):
        wallbrk = pygame.Rect(450 + e, 50 + i, 30, 30)
        if wallbrk not in brick_coord:
            brick_coord.append(wallbrk)
        if wallbrk not in wall_coord:
            wall_coord.append(wallbrk)