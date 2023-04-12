"""
this is the file that will draw our map, this holds a class which is a sprite called Tile
"""

import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    """
    this is the TileDraw class which inherets pygame sprite
    """

    def __init__(self, pos, groups, sprite_type, surf = pygame.Surface((TILESIZE,TILESIZE)) ):
        """
        this function accepts a position and a sprite group, this shows where to place everything
        """
        super().__init__(groups)
        self.sprite_type = sprite_type

        self.image = surf
        if sprite_type == 'object':
            self.rect = self.image.get_rect(topleft = (pos[0],pos[1] - TILESIZE))
        else:
            self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)

