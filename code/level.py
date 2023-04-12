"""
this is the level file

this contains a level class and level class is the most important part of this game, everything that is in the level class will be rendered
"""


import pygame
from settings import *
from tile import Tile
from player import Player
#from debug import debug
from pytmx.util_pygame import load_pygame

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

        self.tmx_data = load_pygame('../data/tmx/map.tmx')

        # making the map
        self.make_map()

    def make_map(self):
        """
        this is the function that will draw our map based off of the world map array in settings
        """
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer,'data'):
                print(layer.name)
                if layer.name == 'Floor':
                    '''for x,y,surf in layer.tiles():
                        pos = (x * TILESIZE, y * TILESIZE)
                        Tile(pos = pos, surf = surf, sprite_type='not', groups = [self.visible_sprites])'''
                    pass
                elif layer.name == 'Player':
                    for x,y,surf in layer.tiles():
                        pos = (x * TILESIZE, y * TILESIZE)
                        self.player = Player(pos, [self.visible_sprites], self.obstacle_sprites)
                else:
                    for x,y,surf in layer.tiles():
                        pos = (x * TILESIZE, y * TILESIZE)
                        Tile(pos = pos, surf = surf, sprite_type='not', groups = [self.visible_sprites, self.obstacle_sprites])

        self.player = Player(pos, [self.visible_sprites], self.obstacle_sprites)

    def run(self):
        """
        this method will update and draw the game
        """

        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

        # need to get rid of this later
        #debug(self.player.direction)


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        self.floor_surf = pygame.image.load('../data/floor/floor.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))


    def custom_draw(self, player): 
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
    


