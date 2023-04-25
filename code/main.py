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
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("SWE PROJECT")
        self.clock = pygame.time.Clock()

        # setting the title of our game

        # if we want then we can set an icon as well
        # Icon = pygame.image.laod("some icon file")
        # pygame.display.set_icon(Icon)

        # making the level
        self.level_one = Level()

        #OST
        main_sound  = pygame.mixer.Sound('../audio/main_ost.ogg')
        main_sound.set_volume(0.7)
        main_sound.play(loops=-1)

    def run(self):
        """
        this is the initial running of the game
        """

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(WATER_COLOR)
            self.level_one.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
