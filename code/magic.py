import pygame
from settings import *
from random import randint


class MagicPlayer:
    """
    this is so that the player can use the magic functionality in the game
    """

    def __init__(self, animation_player):
        """
        initializing the animation player for magic
        """

        self.animation_player = animation_player
        self.sounds = {
            "heal": pygame.mixer.Sound("../audio/heal.wav"),
            "flame": pygame.mixer.Sound("../audio/fire.wav"),
        }
        for x in self.sounds.values():
            x.set_volume(0.6)

    def heal(self, player, strength, cost, groups):
        """
        making the heal spell work to increase player health
        """

        # player can only use spell if energy is over the cost amount
        if player.energy >= cost:
            self.sounds["heal"].play()
            player.health = player.health + strength
            player.energy = player.energy - cost

            # reseting the player health if it goes over
            if player.health >= player.stats["health"]:
                player.health = player.stats["health"]

            # making the animations
            self.animation_player.create_particles("aura", player.rect.center, groups)
            self.animation_player.create_particles("heal", player.rect.center, groups)

    def flame(self, player, cost, groups):
        """
        this is the flame spell that will allow the player to attack enemies
        """

        # checking if player has enough cost for flame
        if player.energy >= cost:
            self.sounds["flame"].play()
            if player.status.split("_")[0] == "right":
                direction = pygame.math.Vector2(1, 0)
            elif player.status.split("_")[0] == "left":
                direction = pygame.math.Vector2(-1, 0)
            elif player.status.split("_")[0] == "up":
                direction = pygame.math.Vector2(0, -1)
            else:
                direction = pygame.math.Vector2(0, 1)

        # going through the directions to check which way the spell should go
        for i in range(1, 6):
            if direction.x:  # horizontal
                offset_x = (direction.x * i) * TILESIZE
                x = (
                    player.rect.centerx
                    + offset_x
                    + randint(-TILESIZE // 3, TILESIZE // 3)
                )
                y = player.rect.centery + randint(-TILESIZE // 3, TILESIZE // 3)
                self.animation_player.create_particles("flame", (x, y), groups)
            else:  # vertical
                offset_y = (direction.y * i) * TILESIZE
                x = player.rect.centerx + randint(-TILESIZE // 3, TILESIZE // 3)
                y = (
                    player.rect.centery
                    + offset_y
                    + randint(-TILESIZE // 3, TILESIZE // 3)
                )
                self.animation_player.create_particles("flame", (x, y), groups)
