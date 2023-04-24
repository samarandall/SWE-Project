import pygame


class Entity(pygame.sprite.Sprite):
    """
    entity class that makes an actual entity sprite
    this is what the Enemy class is based off of
    """

    def __init__(self, groups):
        """
        initializing everything for the Entity class
        """

        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.direction = pygame.math.Vector2()

    def move(self, speed):
        """
        entity movement all setup
        """

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

            self.hitbox.x += self.direction.x * speed
            self.collision("horizontal")
            self.hitbox.y += self.direction.y * speed
            self.collision("vertical")
            self.rect.center = self.hitbox.center

    def collision(self, direction):
        """
        making collisions work with entities
        """

        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    # right
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    # left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    # down
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    # up
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
