import pygame
from settings import *
from entity import Entity
from support import *


class Enemy(Entity):
    """
    this is the class for how our enemies will work and it is an extension of the entity class
    """

    def __init__(
        self,
        monster_name,
        pos,
        groups,
        obstacle_sprites,
        damage_player,
        trigger_death_particles,
    ):
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

        # so player can interact
        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 400
        self.damage_player = damage_player
        self.trigger_death_particles = trigger_death_particles

        # invincibility timer for the enemies
        self.vulnerable = True
        self.hit_time = None
        self.invincibility_duration = 300

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
            self.damage_player(self.attack_damage, self.attack_type)
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

        # checking if vulnerable or not and deciding what to do
        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def cooldown(self):
        """
        there needs to be cooldown between attacks and this covers that
        """

        # getting the current time
        current_time = pygame.time.get_ticks()

        if not self.can_attack:
            current_time = pygame.time.get_ticks()
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True

        if not self.vulnerable:
            if current_time - self.hit_time >= self.invincibility_duration:
                self.vulnerable = True

    def get_damage(self, player, attack_type):
        """
        this is to get the damage from the player
        """

        if self.vulnerable:
            self.direction = self.get_player_distance_direction(player)[1]
            if attack_type == "weapon":
                self.health -= player.get_full_weapon_damage()
            else:
                # for right now this is a pass but we will do this later for magic
                pass
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

    def hit_reaction(self):
        """
        animation for being hit
        """

        if not self.vulnerable:
            self.direction *= -self.resistance

    def update(self):
        """
        updating the enemy movement
        """

        self.hit_reaction()
        self.move(self.speed)
        self.animate()
        self.cooldown()
        self.check_death()

    def enemy_update(self, player):
        """
        updating enemy status
        """

        self.get_status(player)
        self.actions(player)
