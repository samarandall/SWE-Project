"""
this is our main file for our game

this file contains our main game loop, game class, and the 
main function which will run our game
"""

import pygame, sys
from settings import *
from level import Level


class Game:
    """
    this is our initial class which will run the game
    """

    def __init__(self):
        """
        this is initial setup for our game
        """

        pygame.init()
        self.screen_width, self.screen_height = WIDTH, HEIGHT
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
        pygame.display.set_caption("SWE PROJECT - The Battle for Sugar Rush : Dallas Gere, Sam Randall, Victor Ekpenyong")
        self.clock = pygame.time.Clock()

        # setting the title of our game

        # if we want then we can set an icon as well
        # Icon = pygame.image.laod("some icon file")
        # pygame.display.set_icon(Icon)

        # making the level
        self.level_one = Level()


    def draw_start_menu(self):
        self.screen.fill((43, 26, 7))
        title_font = pygame.font.Font('../graphics/font/joystix.ttf', 60)
        start_font = pygame.font.Font('../graphics/font/joystix.ttf', 40)
        enter_font = pygame.font.Font('../graphics/font/joystix.ttf', 15)
        title = title_font.render('The Battle for Sugar Rush', True, (205, 86, 156))
        title_rect = title.get_rect()
        title_rect.center = (self.screen_width // 2, (self.screen_height // 2) - (self.screen_height // 8))
        start_button = start_font.render('Start', True, (255, 255, 255))
        start_button_rect = start_button.get_rect()
        start_button_rect.center = (self.screen_width // 2, (self.screen_height // 2) + (self.screen_height // 4))
        enter = enter_font.render('(Enter)', True, (205, 86, 156))
        enter_rect = enter.get_rect()
        enter_rect.center = (self.screen_width // 2, (self.screen_height // 2) + (self.screen_height // 3))
        self.screen.blit(title, title_rect)
        self.screen.blit(start_button, start_button_rect)
        self.screen.blit(enter, enter_rect)
        pygame.display.update()
    
    def draw_pause_menu(self):
        self.screen.fill((43, 26, 7))
        title_font = pygame.font.Font('../graphics/font/joystix.ttf', 80)
        button_font = pygame.font.Font('../graphics/font/joystix.ttf', 60)
        r_font = pygame.font.Font('../graphics/font/joystix.ttf', 25)
        title = title_font.render('PAUSED', True, (205, 86, 156))
        title_rect = title.get_rect()
        title_rect.center = (self.screen_width // 2, (self.screen_height // 2) - (self.screen_height // 8))
        resume_button = button_font.render('Resume', True, (255, 255, 255))
        resume_button_rect = resume_button.get_rect()
        resume_button_rect.center = (self.screen_width // 2, (self.screen_height // 2) + (self.screen_height // 4))
        r = r_font.render('(r)', True, (205, 86, 156))
        r_rect = r.get_rect()
        r_rect.center = (self.screen_width // 2, (self.screen_height // 2) + (self.screen_height // 3))
        self.screen.blit(title, title_rect)
        self.screen.blit(resume_button, resume_button_rect)
        self.screen.blit(r, r_rect)
        pygame.display.update()
    
    def draw_game_over(self):
        self.screen.fill((43, 26, 7))
        title_font = pygame.font.Font('../graphics/font/joystix.ttf', 80)
        button_font = pygame.font.Font('../graphics/font/joystix.ttf', 40)
        enter_font = pygame.font.Font('../graphics/font/joystix.ttf', 15)
        title = title_font.render('GAME OVER', True, (159, 0, 24))
        title_rect = title.get_rect()
        title_rect.center = (self.screen_width // 2, (self.screen_height // 2) - (self.screen_height // 8))
        start_menu = button_font.render('Start Menu', True, (255, 255, 255))
        start_menu_rect = start_menu.get_rect()
        start_menu_rect.center = (self.screen_width // 2, (self.screen_height // 2) + (self.screen_height // 4))
        enter = enter_font.render('(Space)', True, (205, 86, 156))
        enter_rect = enter.get_rect()
        enter_rect.center = (self.screen_width // 2, (self.screen_height // 2) + (self.screen_height // 3))
        self.screen.blit(title, title_rect)
        self.screen.blit(start_menu, start_menu_rect)
        self.screen.blit(enter, enter_rect)
        pygame.display.update()
        

    def run(self):
        """
        this is the initial running of the game
        """

        while True:
            keys = pygame.key.get_pressed()
            self.game_state = self.level_one.get_game_state()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.VIDEORESIZE:
                    # Update the screen size
                    self.screen_width, self.screen_height = event.size
                    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
            if self.game_state == 'start_menu':
                self.draw_start_menu()
                if keys[pygame.K_RETURN]:
                    self.level_one = Level()
                    self.level_one.update_game_state('game')
            elif self.game_state == 'pause':
                self.draw_pause_menu()
                self.level_one.pause_the_level()
                if keys[pygame.K_r]:
                    self.level_one.unpause_the_level()
                    self.level_one.update_game_state('game')
                if keys[pygame.K_ESCAPE]:
                    self.level_one.update_game_state('start_menu')
            elif self.game_state == 'game_over':
                self.draw_game_over()
                if keys[pygame.K_SPACE]:
                    self.level_one.update_game_state('start_menu')
            else:
                self.screen.fill("black")
                self.level_one.run()
                pygame.display.update()
                self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
