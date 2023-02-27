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

    def __init__(self, pos, groups, obstacle_sprites):
        """
        this function accepts a position and a sprite group, this shows where to place everything
        """

        # this is needed to initialize sprites
        # this initializes the TileDraw class
        super().__init__(groups)

        # these variables are always needed for sprites
        self.image = pygame.image.load(
            "../graphics/map_assets/player.png"
        ).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

        # giving the player the ability to walk in a certain direction
        self.direction = pygame.math.Vector2()

        # giving speed of player
        self.speed = 5

        # making the obstacle sprites attribute
        self.obstacle_sprites = obstacle_sprites

    def keyboard_input(self):
        """
        this function is getting keys from the user input and making them do something
        """

        # these are all the possible keys that could be pressed
        keys = pygame.key.get_pressed()

        # this is assigning the keys being pressed to a certain direction
        # the else makes it so that if there are no keys being pressed then
        # player stays still
        # this one is for vertical movements
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        # this one is for horizontal movements
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move_player(self, speed):
        """
        this is the function that
        """
        #
        # if self.direction.magnitude() != 0:
        #     self.direction = self.direction.x * speed
        #
        # self.rect.x += self.direction.x * speed
        # self.colission("horizontal")
        # self.rect.y += self.direction.y * speed
        # self.collision("vertical")
        #
        self.rect.center += self.direction * speed

    # def update_player_movement(self):
    def update(self):
        """
        this function will update the players movement
        """

        self.keyboard_input()
        self.move_player(self.speed)
