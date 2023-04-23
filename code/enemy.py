import pygame
from settings import *
from entity import Entity
from support import *


class Enemy(Entity):
    """
    this is the class for how our enemies will work and it is an extension of the entity class
    """

    def __init__(self, monster_name, pos, groups, obstacle_sprites):
        """
        setting up the init for our enemies to be initialized
        """

        # initializing the enemy name
        super().__init__(groups)
        self.sprite_type = "enemy"

        # graphics for the enemies
        self.import_graphics(monster_name)
        self.status = "idle"
        self.image = self.animations[self.status][self.frame_index]

        # setting up enemy stats
        self.monster_name = monster_name
        monster_info = monster_data[self.monster_name]
        self.health = monster_info["health"]
        self.exp = monster_info["exp"]
        self.speed = monster_info["speed"]
        self.attack_damage = monster_info["damage"]
        self.resistance = monster_info["resistance"]
        self.attack_radius = monster_info["attack_radius"]
        self.notice_radius = monster_info["notice_radius"]
        self.attack_type = monster_info["attack_type"]

        # this is the initialization for how the players will interact with the enemies
        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 400

        # setting up enemy movement
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)
        self.obstacle_sprites = obstacle_sprites

    def import_graphics(self, name):
        """
        this imports all the graphics that we need for the monsters
        """

        # making the animations
        self.animations = {"idle": [], "move": [], "attack": []}

        # the path for the particular monster
        main_path = f"../graphics/monsters/{name}/"

        # looping over the animations
        for i in self.animations.keys():
            self.animations[i] = import_folder(main_path + i)
