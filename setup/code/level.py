"""
this is the level file

this contains a level class and level class is the most important part of this game, everything that is in the level class will be rendered
"""

import pygame


class Level:
    """
    definition of the very important Level class
    """

    def __init__(self):
        """
        initializing all the level attributes
        """

        # these are the sprite groups
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # we need a surface to display
        self.display_surface = pygame.display.get_surface()

    def run(self):
        """
        this method will update and draw the game
        """

        pass
