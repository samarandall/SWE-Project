"""
this is the file that will draw our map, this holds a class which is a sprite called Tile
"""

import pygame
from settings import *


class TileDraw(pygame.sprite.Sprite):
    """
    this is the TileDraw class which inherets pygame sprite
    """

    def __init__(self, pos, groups):
        """
        this function accepts a position and a sprite group, this shows where to place everything
        """

        # this is needed to initialize sprites
        # this initializes the TileDraw class
        super().__init__(groups)

        # these variables are always needed for sprites
        self.image = pygame.image.load(
            "../graphics/map_assets/rock.png"
        ).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
