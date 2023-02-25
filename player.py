"""
This file contains a player class which will initialize our player

This is similair to the TileDraw class
"""

import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    """
    this is the Player class which inherets pygame sprite
    """

    def __init__(self, pos, groups):
        """
        this function accepts a position and a sprite group, this shows where to place everything
        """

        # this is needed to initialize sprites
        # this initializes the TileDraw class
        super().__init__(groups)

        # these variables are always needed for sprites
        self.image = pygame.image.load("../graphics/test/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
