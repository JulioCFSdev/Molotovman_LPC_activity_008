import pygame
from Config import Colors, Constants, screen

class Main_screen():
    def menu():
        global menu_stats
        play_txt = Constants.PYFONT.render("Play", True, Colors.BLACK)
        quit_txt = Constants.PYFONT.render("Quit", True, Colors.BLACK)
        menu_stats = True
        click = False

        while menu_stats:
            screen.fill(Colors.WHITE)
            menu_img = pygame.image.load("img/menu_bg.jpg")
            mx, my = pygame.mouse.get_pos()

            start_button = pygame.Rect((Constants.SCREEN_SIZE[1] / 2) + 25, 600, 145, 47)
            quit_button = pygame.Rect((Constants.SCREEN_SIZE[1] / 2) + 25, 700, 145, 47)
            screen.blit(menu_img, (0, 0))
            screen.blit(play_txt, ((Constants.SCREEN_SIZE[1] / 2) + 45, 600))
            screen.blit(quit_txt, ((Constants.SCREEN_SIZE[1] / 2) + 45, 700))

            if start_button.collidepoint((mx, my)):
                if click:
                    menu_stats = False
            if quit_button.collidepoint((mx, my)):
                if click:
                    pygame.quit()
                    exit()

            click = False
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

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                        
            pygame.time.Clock().tick(Constants.CLOCK_TICK)
            pygame.display.update()
