import pygame

class Bricks:
    def images(self):
        img_arenabrk = pygame.image.load("sprites/arena_block.png")
        img_wallblock = pygame.image.load("sprites/wall_block.png")

        return(img_arenabrk, img_wallblock)
