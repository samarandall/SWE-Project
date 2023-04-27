import pygame
from settings import *


class UI:
    def __init__(self):
        # getting the surface and the font
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # making the health bar
        self.health_bar_rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.energy_bar_rect = pygame.Rect(10, 34, ENERGY_BAR_WIDTH, BAR_HEIGHT)

        # magic info converted into graphics
        self.magic_graphics = []
        for magic in magic_data.values():
            magic = pygame.image.load(magic["graphic"]).convert_alpha()
            self.magic_graphics.append(magic)

        # weapon dictionary made into graphics
        self.weapon_graphics = []
        for weapon in weapon_data.values():
            path = weapon["graphic"]
            weapon = pygame.image.load(path).convert_alpha()
            self.weapon_graphics.append(weapon)
        
        self.screen_width, self.screen_height = WIDTH, HEIGHT

    def show_bar(self, current, max_amount, bg_rect, color):
        """
        this function should show the bar for player information
        """

        # getting the backgroung
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        # converting stat to pixel
        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        # drawing the actual bar itself
        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)

    def show_exp(self, exp):
        """
        this function should show the experience for the player
        """

        # getting the text to work
        text_surf = self.font.render(str(int(exp)), False, TEXT_COLOR)
        x = self.display_surface.get_size()[0] - 20
        y = self.display_surface.get_size()[1] - 20
        text_rect = text_surf.get_rect(bottomright=(x, y))

        # drawing the actual experience bar
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(20, 20))
        self.display_surface.blit(text_surf, text_rect)
        pygame.draw.rect(
            self.display_surface, UI_BORDER_COLOR, text_rect.inflate(20, 20), 3
        )

    def selection_box(self, left, top, has_switched):
        """
        this should give the selection box for where to select and hit things
        """

        # making the background rectangle for the
        bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        # drawing the border condition
        if has_switched:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE, bg_rect, 3)
        else:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)

        return bg_rect

    def magic_overlay(self, magic_index, has_switched):
        """
        making the magic ui
        """

        # this generates everything for the magic overlay
        bg_rect = self.selection_box(80, (self.screen_height / 10), has_switched)
        magic_surface = self.magic_graphics[magic_index]
        magic_rect = magic_surface.get_rect(center=bg_rect.center)
        self.display_surface.blit(magic_surface, magic_rect)

    def weapon_overlay(self, weapon_index, has_switched):
        """
        making the weapon overlay better
        """

        # making all the weapon overlay
        bg_rect = self.selection_box(10, (self.screen_height / 8), has_switched)
        weapon_surf = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surf.get_rect(center=bg_rect.center)
        self.display_surface.blit(weapon_surf, weapon_rect)

    def display(self, player):
        """
        displaying the bar for player info
        """

        # displaying the bar
        self.show_bar(
            player.health, player.stats["health"], self.health_bar_rect, HEALTH_COLOR
        )
        self.show_bar(
            player.energy, player.stats["energy"], self.energy_bar_rect, ENERGY_COLOR
        )

        # showing player exp
        self.show_exp(player.exp)

        # showing weapon ui
        self.weapon_overlay(player.weapon_index, not player.can_switch_weapon)

        # showing magic ui
        self.magic_overlay(player.magic_index, not player.can_switch_magic)
