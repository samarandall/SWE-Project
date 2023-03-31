"""
this is the level file

this contains a level class and level class is the most important part of this game, everything that is in the level class will be rendered
"""


import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug


class Level:
    """
    definition of the very important Level class
    """

    def __init__(self):
        """
        initializing all the level attributes
        """

        # we need a surface to display
        self.display_surface = pygame.display.get_surface()

        # these are the sprite groups
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # making the map
        self.make_map()

    def make_map(self):
        """
        this is the function that will draw our map based off of the world map array in settings
        """

        for index, i in enumerate(WORLD_MAP):
            for jindex, j in enumerate(i):
                x = jindex * TILESIZE
                y = index * TILESIZE

                if j == "x":
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                if j == "p":
                    self.player = Player(
                        (x, y), [self.visible_sprites], self.obstacle_sprites
                    )

    def run(self):
        """
        this method will update and draw the game
        """

        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

        # need to get rid of this later
        debug(self.player.direction)


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
    
    def custom_draw(self, player):
        
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
    


