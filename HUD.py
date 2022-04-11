import pygame
from Config import screen
from Config import Colors

class Hud:

    def draw(self, scr_sv, scr_am):
        hud_image = pygame.image.load("sprites/Scenario/HUD.png")
        screen.blit(hud_image, (0, 745))

        score_sv_font = pygame.font.Font("img/upheavtt.ttf", 50)
        score_sv_text = score_sv_font.render(scr_sv, True, Colors.WHITE)
        score_sv_text_rect = score_sv_text.get_rect()
        score_sv_text_rect.center = (154, 767)
        screen.blit(score_sv_text, score_sv_text_rect)

        score_am_font = pygame.font.Font("img/upheavtt.ttf", 50)
        score_am_text = score_am_font.render(scr_am, True, Colors.WHITE)
        score_am_text_rect = score_am_text.get_rect()
        score_am_text_rect.center = (801, 767)
        screen.blit(score_am_text, score_am_text_rect)



