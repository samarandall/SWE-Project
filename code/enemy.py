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

    def get_player_distance_direction(self, player):
        """
        this function will help determine where the player is in regards to the enemy
        """

        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()

        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()

        return (distance, direction)

    def get_status(self, player):
        """
        this shows whether the player is in distance or not
        """

        distance = self.get_player_distance_direction(player)[0]

        if distance <= self.attack_radius and self.can_attack:
            if self.status != "attack":
                self.frame_index = 0
            self.status = "attack"
        elif distance <= self.notice_radius:
            self.status = "move"
        else:
            self.status = "idle"

    def actions(self, player):
        """
        actions depending on where the player is
        """

        # checking what the status is and deciding based off that what the player can do
        if self.status == "attack":
            self.attack_time = pygame.time.get_ticks()
        elif self.status == "move":
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()

    def animate(self):
        """
        actually animating everything
        """

        animation = self.animations[self.status]
        self.frame_index += self.animation_speed

        # checking what the enemy can do or not
        if self.frame_index >= len(animation):
            if self.status == "attack":
                self.can_attack = False
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

    def cooldown(self):
        """
        there needs to be cooldown between attacks and this covers that
        """

        if not self.can_attack:
            current_time = pygame.time.get_ticks()
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True

    def update(self):
        """
        updating the enemy movement
        """

        self.move(self.speed)
        self.animate()
        self.cooldown()

    def enemy_update(self, player):
        """
        updating enemy status
        """

        self.get_status(player)
        self.actions(player)
