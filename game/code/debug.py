"""
this file will be used to help debug the game

this will give us game information and will not affect the game

run debug in the main game loop and print and important information
"""

import pygame

pygame.init()
font = pygame.font.Font(None, 30)


def debug(info, y=10, x=10):
    """
    the main debugging function
    """

    display_surface = pygame.display.get_surface()
    debug_surface = font.render(str(info), True, "white")
    debug_rectangle = debug_surface.get_rect(topleft=(x, y))
    pygame.draw.rect(display_surface, "Black", debug_rectangle)
    display_surface.blit(debug_surface, debug_rectangle)
