"""
this is the level file

this contains a level class and level class is the most important part of this game, everything that is in the level class will be rendered
"""


import pygame
from settings import *
from tile import Tile
from player import Player

from pytmx.util_pygame import load_pygame
from support import *
from random import choice, randint
from weapon import Weapon
from ui import UI
from enemy import Enemy
from particle import AnimationPlayer
from magic import MagicPlayer
import random


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

        # for attacking sprites
        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        # ui
        self.ui = UI()

        # making the map
        self.make_map()

        # particles
        self.animation_player = AnimationPlayer()

        # magic animations
        self.magic_player = MagicPlayer(self.animation_player)

        # Is the Level Paused
        self.pause = False

        # for spawning enemies in the game every 3 seconds
        # 3000 milliseconds is 3 seconds
        self.SPAWN_ENEMY_EVENT = pygame.USEREVENT + 1
        # pygame.time.set_timer(self.SPAWN_ENEMY_EVENT, 3000)
        pygame.time.set_timer(self.SPAWN_ENEMY_EVENT, 20000)
        # pygame.time.set_timer(self.SPAWN_ENEMY_EVENT, 200)
        self.enemy_list = ["bamboo", "spirit", "raccoon", "squid"]
        self.enemies = []

    def spawn_enemy(self):
        x = random.randint((WIDTH // 2) - 5, (WIDTH // 2) + 10)
        y = random.randint((HEIGHT // 2) - 5, (HEIGHT // 2) + 10)
        monster_name = random.choice(self.enemy_list)
        new_enemy = Enemy(
            monster_name,
            (x, y),
            [self.visible_sprites, self.attackable_sprites],
            self.obstacle_sprites,
            self.damage_player,
            self.trigger_death_particles,
            self.add_exp,
        )
        self.enemies.append(new_enemy)

        for enemy in self.enemies:
            enemy.spawn_update()

    def make_map(self):
        """
        this is the function that will draw our map based off of the world map array in settings
        """

        # for layer in self.tmx_data.visible_layers:
        #     if hasattr(layer, "data"):
        #         print(layer.name)
        #         if layer.name == "Floor":
        #             """for x,y,surf in layer.tiles():
        #             pos = (x * TILESIZE, y * TILESIZE)
        #             Tile(pos = pos, surf = surf, sprite_type='not', groups = [self.visible_sprites])
        #             """
        #             pass
        #         elif layer.name == "Player":
        #             for x, y, surf in layer.tiles():
        #                 pos = (x * TILESIZE, y * TILESIZE)
        #                 self.player = Player(
        #                     pos,
        #                     [self.visible_sprites],
        #                     self.obstacle_sprites,
        #                     self.create_attack,
        #                     self.destroy_attack,
        #                 )
        #         else:
        #             for x, y, surf in layer.tiles():
        #                 pos = (x * TILESIZE, y * TILESIZE)
        #                 Tile(
        #                     pos=pos,
        #                     surf=surf,
        #                     sprite_type="not",
        #                     groups=[self.visible_sprites, self.obstacle_sprites],
        #                 )

        # self.player = Player(
        #     pos,
        #     [self.visible_sprites],
        #     self.obstacle_sprites,
        #     self.create_attack,
        #     self.destroy_attack,
        # )

        # how the map is supposed to look
        layouts = {
            "boundary": import_csv_layout("../map/map_FloorBlocks.csv"),
            "grass": import_csv_layout("../map/map_Grass.csv"),
            "object": import_csv_layout("../map/map_Objects.csv"),
            "entities": import_csv_layout("../map/map_Entities.csv"),
        }

        # the graphics for the map
        graphics = {
            "grass": import_folder("../graphics/Grass"),
            "objects": import_folder("../graphics/objects"),
        }

        # this iterates through and draws the map
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != "-1":
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == "boundary":
                            Tile((x, y), [self.obstacle_sprites], "invisible")
                        if style == "grass":
                            random_grass_image = choice(graphics["grass"])
                            Tile(
                                (x, y),
                                [
                                    self.visible_sprites,
                                    self.obstacle_sprites,
                                    self.attackable_sprites,
                                ],
                                "grass",
                                random_grass_image,
                            )

                        if style == "object":
                            surf = graphics["objects"][int(col)]
                            Tile(
                                (x, y),
                                [self.visible_sprites, self.obstacle_sprites],
                                "object",
                                surf,
                            )

                    if style == "entities":
                        if col == "394":
                            self.player = Player(
                                (x, y),
                                [self.visible_sprites],
                                self.obstacle_sprites,
                                self.create_attack,
                                self.destroy_attack,
                                self.create_magic,
                            )
                        else:
                            if col == "390":
                                monster_name = "bamboo"
                            elif col == "391":
                                monster_name = "spirit"
                            elif col == "392":
                                monster_name = "raccoon"
                            else:
                                monster_name = "squid"
                            Enemy(
                                monster_name,
                                (x, y),
                                [self.visible_sprites, self.attackable_sprites],
                                self.obstacle_sprites,
                                self.damage_player,
                                self.trigger_death_particles,
                                self.add_exp,
                            )

    def create_attack(self):
        """
        this creates an attack on keypress
        """

        self.current_attack = Weapon(
            self.player, [self.visible_sprites, self.attack_sprites]
        )

    def destroy_attack(self):
        """
        this stops the attack
        """

        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def create_magic(self, style, strength, cost):
        """
        this creates a magic entity
        """

        # the healing spell
        if style == "heal":
            self.magic_player.heal(self.player, strength, cost, [self.visible_sprites])

        # the flame spell
        if style == "flame":
            self.magic_player.flame(
                self.player, cost, [self.visible_sprites, self.attack_sprites]
            )

    def trigger_death_particles(self, pos, particle_type):
        """
        trigger death particles for sprites that are enemies
        """

        self.animation_player.create_particles(particle_type, pos, self.visible_sprites)

    def player_attack_logic(self):
        """
        how the player attacks will work with the enemies
        """

        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(
                    attack_sprite, self.attackable_sprites, False
                )
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        if target_sprite.sprite_type == "grass":
                            pos = target_sprite.rect.center
                            offset = pygame.math.Vector2(0, 75)
                            for i in range(randint(3, 6)):
                                self.animation_player.create_grass_particles(
                                    pos - offset, [self.visible_sprites]
                                )
                            target_sprite.kill()
                        else:
                            target_sprite.get_damage(
                                self.player, attack_sprite.sprite_type
                            )

    def damage_player(self, amount, attack_type):
        """
        how the player takes damage from the enemy
        """

        # if self.player.vulnerable:
        #     self.player.health -= amount
        #     self.player.vulnerable = False
        #     self.player.hurt_time = pygame.time.get_ticks()
        #     self.animation_player.create_particles(
        #         attack_type, self.player.rect.center, [self.visible_sprites]
        #     )
        # if self.player.health <= 0:
        #     self.update_game_state("game_over")
        pass

    def get_game_state(self):
        return self.player.get_game_state()

    def update_game_state(self, state):
        self.player.update_game_state(state)

    def health_status(self):
        if self.player.health < 50:
            return True
        else:
            return False

    def add_exp(self, amount):
        """
        this function adds the player score with the amount they get for killing an enemy
        """

        # communicating with the player class to add an extra amount
        self.player.exp += amount

    def run(self):
        """
        this method will update and draw the game
        """

        if self.pause != True:
            self.visible_sprites.custom_draw(self.player)
            self.visible_sprites.update()
            self.visible_sprites.enemy_update(self.player)
            self.player_attack_logic()
            self.ui.display(self.player)

    def pause_the_level(self):
        self.pause = True

    def unpause_the_level(self):
        self.pause = False

    def get_player_score(self):
        return self.player.exp


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # this is the old way that was breaking the game
        # self.floor_surf = pygame.image.load("../data/floor/floor.png").convert()

        self.floor_surf = pygame.image.load("../graphics/tilemap/ground.png").convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

    def enemy_update(self, player):
        enemy_sprites = [
            sprite
            for sprite in self.sprites()
            if hasattr(sprite, "sprite_type") and sprite.sprite_type == "enemy"
        ]
        for enemy in enemy_sprites:
            enemy.enemy_update(player)
