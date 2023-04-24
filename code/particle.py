import pygame
from support import import_folder
from random import choice


class AnimationPlayer:
    """
    importing everything
    """

    def __init__(self):
        self.frames = {
            # magic imports for the animations
            "flame": import_folder("../graphics/particles/flame/frames"),
            "aura": import_folder("../graphics/particles/aura"),
            "heal": import_folder("../graphics/particles/heal/frames"),
            # attacks imports for the animations
            "claw": import_folder("../graphics/particles/claw"),
            "slash": import_folder("../graphics/particles/slash"),
            "sparkle": import_folder("../graphics/particles/sparkle"),
            "leaf_attack": import_folder("../graphics/particles/leaf_attack"),
            "thunder": import_folder("../graphics/particles/thunder"),
            # monster deaths imports for the animations
            "squid": import_folder("../graphics/particles/smoke_orange"),
            "raccoon": import_folder("../graphics/particles/raccoon"),
            "spirit": import_folder("../graphics/particles/nova"),
            "bamboo": import_folder("../graphics/particles/bamboo"),
            # leafs imports for the animations
            "leaf": (
                import_folder("../graphics/particles/leaf1"),
                import_folder("../graphics/particles/leaf2"),
                import_folder("../graphics/particles/leaf3"),
                import_folder("../graphics/particles/leaf4"),
                import_folder("../graphics/particles/leaf5"),
                import_folder("../graphics/particles/leaf6"),
                self.reflect_images(import_folder("../graphics/particles/leaf1")),
                self.reflect_images(import_folder("../graphics/particles/leaf2")),
                self.reflect_images(import_folder("../graphics/particles/leaf3")),
                self.reflect_images(import_folder("../graphics/particles/leaf4")),
                self.reflect_images(import_folder("../graphics/particles/leaf5")),
                self.reflect_images(import_folder("../graphics/particles/leaf6")),
            ),
        }

    def reflect_images(self, frames):
        new_frames = []

        for i in frames:
            flipped_frame = pygame.transform.flip(i, True, False)
            new_frames.append(flipped_frame)

        return new_frames

    def create_grass_particles(self, pos, groups):
        """
        creating particles for going over grass
        """

        animation_frames = choice(self.frames["leaf"])
        ParticleEffect(pos, animation_frames, groups)

    def create_particles(self, animation_type, pos, groups):
        """
        creating particles for everything else
        """

        animation_frames = self.frames[animation_type]
        ParticleEffect(pos, animation_frames, groups)


class ParticleEffect(pygame.sprite.Sprite):
    """
    particle effects class that makes the effects
    """

    def __init__(self, pos, animation_frames, groups):
        # super init
        super().__init__(groups)

        # initializing everything for the particle effects
        self.sprite_type = "magic"
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

    def animate(self):
        """
        animating everything
        """

        # initializing frame index
        self.frame_index += self.animation_speed

        # killing effect if it is no longer needed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()
