"""
this file will contain code to allow the player to have weapons    
"""

import pygame


class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        direction = player.status.split("_")[0]

        # graphics for the weapons
        full_path = f"../graphics/weapons/{player.weapon}/{direction}.png"
        self.image = pygame.image.load(full_path).convert_alpha()

        # placement for the weapon
        if direction == "right":
            self.rect = self.image.get_rect(
                midleft=player.rect.midright + pygame.math.Vector2(0, 16)
            )
        elif direction == "left":
            self.rect = self.image.get_rect(
                midright=player.rect.midleft + pygame.math.Vector2(0, 16)
            )
        elif direction == "down":
            self.rect = self.image.get_rect(
                midtop=player.rect.midbottom + pygame.math.Vector2(-10, 0)
            )
        else:
            self.rect = self.image.get_rect(
                midbottom=player.rect.midtop + pygame.math.Vector2(-10, 0)
            )
