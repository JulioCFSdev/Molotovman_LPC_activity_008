import pygame
from Config import Colors, Constants, screen

class Main_screen():
    def menu():
        global menu_stats
        font = pygame.font.Font(Constants.FONT, 50)
        play_txt = font.render("Press Enter to Play", True, Colors.BLACK)
        quit_txt = font.render("Press ESC to Quit", True, Colors.BLACK)
        menu_stats = True

        while menu_stats:
            screen.fill(Colors.WHITE)
            menu_img = pygame.image.load("img/menu_bg.jpg")
            screen.blit(menu_img, (0, 0))
            screen.blit(play_txt, ((Constants.SCREEN_SIZE[1] / 2) - 80, 600))
            screen.blit(quit_txt, ((Constants.SCREEN_SIZE[1] / 2) - 80, 700))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                    if event.key == pygame.K_RETURN:
                        menu_stats = False
                        
            pygame.time.Clock().tick(Constants.CLOCK_TICK)
            pygame.display.update()
