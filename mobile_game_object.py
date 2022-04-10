import pygame

from Config import screen, brick_coord
from Player import Soviet, American

pygame.init()

class Draw_Players:

    def draw_soviet(self, add_x, add_y, last_key_pressed):
        x = 0
        pos_x_s = 50 + add_x
        pos_y_s = 50 + add_y
        screen.blit(Soviet.soviet_soldier(Soviet, last_key_pressed),(pos_x_s, pos_y_s))
        pygame.draw.rect(screen,(255,0, 0), [pos_x_s + 5, pos_y_s + 15, 36, 50],2)
        obj_rect = pygame.Rect(pos_x_s + 5, pos_y_s + 15, 36, 50)
        obj_soviet = Soviet.soviet_soldier(Soviet, last_key_pressed).get_rect(center=(pos_x_s, pos_y_s))
        while x < len(brick_coord):

            if pygame.Rect.colliderect(obj_rect, brick_coord[x]):

                print((obj_soviet.x, obj_soviet.y))
                print((brick_coord[x].x, brick_coord[x].y))
                print("colidiu")
            x += 1

        return obj_soviet

    def draw_american(self, add_x, add_y, last_key_pressed):
        pos_x_a = 850 + add_x
        pos_y_a = 630 + add_y
        screen.blit(American.american_soldier(American, last_key_pressed),(pos_x_a, pos_y_a))
        pygame.draw.rect(screen,(255,0,0), [pos_x_a + 5, pos_y_a + 15, 36, 50], 2)
        obj_rect = pygame.Rect(pos_x_a + 5, pos_y_a + 15, 36, 50)
        obj_american = American.american_soldier(American, last_key_pressed).get_rect(center=(pos_x_a, pos_y_a))


