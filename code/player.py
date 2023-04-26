"""
This file contains a player class which will initialize our player

This is similair to the TileDraw class
"""

import pygame
from settings import *
from support import import_folder
from entity import Entity
import time


class Player(Entity):
    """
    this is the Player class which inherets pygame sprite
    """

    def __init__(
        self, pos, groups, obstacle_sprites, create_attack, destroy_attack, create_magic
    ):
        """
        this function accepts a position and a sprite group, this shows where to place everything
        """

        # this is needed to initialize sprites
        # this initializes the TileDraw class
        super().__init__(groups)

        # these variables are always needed for sprites
        self.image = pygame.image.load(
            "../sprite_stuff/map_assets/player.png"
        ).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -26)

        # setting up the graphics for player
        self.import_player_assets()
        self.status = "down"
        self.frame_index = 0
        self.animation_speed = 0.15

        # giving the player the ability to walk in a certain direction
        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None

        # making the obstacle sprites attribute
        self.obstacle_sprites = obstacle_sprites

        # initializing everything for the weapons
        self.create_attack = create_attack
        self.destroy_attack = destroy_attack
        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]
        self.can_switch_weapon = True
        self.weapon_switch_time = None
        self.switch_duration_cooldown = 200

        # this is everything for the health bar and player stats
        self.stats = {"health": 100, "energy": 60, "attack": 10, "magic": 4, "speed": 5}
        self.health = self.stats["health"] * 0.5
        self.energy = self.stats["energy"] * 0.8
        self.exp = 123
        self.speed = self.stats["speed"]

        # initializing everything that we need for the magic items
        self.create_magic = create_magic
        self.magic_index = 0
        self.magic = list(magic_data.keys())[self.magic_index]
        self.can_switch_magic = True
        self.magic_switch_time = None

        # damage to enemies stuff
        self.vulnerable = True
        self.hurt_time = None
        self.invulnerability_duration = 500

    def import_player_assets(self):
        character_path = "../graphics/player/"
        self.animations = {
            "up": [],
            "down": [],
            "left": [],
            "right": [],
            "right_idle": [],
            "left_idle": [],
            "up_idle": [],
            "down_idle": [],
            "right_attack": [],
            "left_attack": [],
            "up_attack": [],
            "down_attack": [],
        }

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def keyboard_input(self):
        """
        this function is getting keys from the user input and making them do something
        """

        if not self.attacking:
            # these are all the possible keys that could be pressed
            keys = pygame.key.get_pressed()

            # this is assigning the keys being pressed to a certain direction
            # the else makes it so that if there are no keys being pressed then
            # player stays still
            # this one is for vertical movements
            if keys[pygame.K_UP]:
                self.direction.y = -1
                self.status = "up"
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.status = "down"
            else:
                self.direction.y = 0

            # this one is for horizontal movements
            if keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.status = "right"
            elif keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status = "left"
            else:
                self.direction.x = 0

            # attacking with the space bar
            if keys[pygame.K_SPACE]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.create_attack()
                print("attack")

            # how to use magic with left control
            if keys[pygame.K_LCTRL]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                style = list(magic_data.keys())[self.magic_index]
                strength = (
                    list(magic_data.values())[self.magic_index]["strength"]
                    + self.stats["magic"]
                )
                cost = list(magic_data.values())[self.magic_index]["cost"]
                self.create_magic(style, strength, cost)

            # switching magic with e
            if keys[pygame.K_e] and self.can_switch_magic:
                self.can_switch_magic = False
                self.magic_switch_time = pygame.time.get_ticks()

                if self.magic_index < len(list(magic_data.keys())) - 1:
                    self.magic_index += 1
                else:
                    self.magic_index = 0

                self.magic = list(magic_data.keys())[self.magic_index]

            # key input for weapons
            if keys[pygame.K_q] and self.can_switch_weapon:
                print("weapon")
                self.can_switch_weapon = False
                self.weapon_switch_time = pygame.time.get_ticks()

                if self.weapon_index < len(list(weapon_data.keys())) - 1:
                    self.weapon_index += 1
                else:
                    self.weapon_index = 0

                self.weapon = list(weapon_data.keys())[self.weapon_index]

    def move(self, speed):
        """
        this is the function that
        """
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision("horizontal")
        self.hitbox.y += self.direction.y * speed
        self.collision("vertical")
        self.rect.center = self.hitbox.center

    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not "idle" in self.status and not "attack" in self.status:
                self.status = self.status + "_idle"

        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not "attack" in self.status:
                if "idle" in self.status:
                    self.status = self.status.replace("_idle", "_attack")
                else:
                    self.status = self.status + "_attack"
        else:
            if "attack" in self.status:
                self.status = self.status.replace("_attack", "")

    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        # checking if the player is attacking
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.destroy_attack()

        # checking if the player can switch weapons
        if not self.can_switch_weapon:
            if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
                self.can_switch_weapon = True

        # checking if the player can switch magic
        if not self.can_switch_magic:
            if current_time - self.magic_switch_time >= self.switch_duration_cooldown:
                self.can_switch_magic = True

        # checking if the player is vulnerable or not
        if not self.vulnerable:
            if current_time - self.hurt_time >= self.invulnerability_duration:
                self.vulnerable = True

    def animate(self):
        animation = self.animations[self.status]

        # frame index loop
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # setting the image for the player
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

        # flicker
        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def get_full_weapon_damage(self):
        """
        this will make it so that the enemies recieve damage from the weapons

        this is based off of what type of weapon it is
        """

        # this is calculating the damage based off the weapon
        base_damage = self.stats["attack"]
        weapon_damage = weapon_data[self.weapon]["damage"]

        # returning the calculated weapon damage based off the weapon
        return base_damage + weapon_damage

    def get_full_magic_damage(self):
        """
        this works like the weapon damage function to get the damage for the weapon
        """

        # this is calculating the damage based off the spell
        base_damage = self.stats["magic"]
        spell_damage = magic_data[self.magic]["strength"]

        # returning the calculated spell damage based off the spell
        return base_damage + spell_damage

    def energy_recovery(self):
        """
        recovering energy after spending it over time
        """

        if self.energy < self.stats["energy"]:
            self.energy += 0.01 * self.stats["magic"]
        else:
            self.energy = self.stats["energy"]

    def get_damage(self, enemy, attack):
        """
        this is to get the damage from the enemy
        """

        if self.vulnerable:
            self.direction = self.get_player_distance_direction(enemy)[1]
            if attack == "weapon":
                self.health -= enemy.get_full_weapon_damage()
            else:
                self.health = self.health - enemy.get_full_magic_damage()
            self.hit_time = pygame.time.get_ticks()
            self.vulnerable = False

    def check_death(self):
        """
        killing enemy when health less than 0

        this works very similary to the player health damage death
        """

        if self.health <= 0:
            self.kill()
            self.trigger_death_particles(self.rect.center, self.monster_name)

    # def update_player_movement(self):
    def update(self):
        """
        this function will update the players movement
        """

        self.keyboard_input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)
        self.energy_recovery()
