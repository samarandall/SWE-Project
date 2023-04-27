import unittest
from unittest.mock import MagicMock
from player import Player

import pygame, sys
from settings import *
from level import Level
from enemy import Enemy
import random

class TestPlayer(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        pygame.init()
        self.screen_width, self.screen_height = WIDTH, HEIGHT
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height), pygame.RESIZABLE
        )
        self.clock = pygame.time.Clock()
        keys = pygame.key.get_pressed()

    
    def setUp(self):
        self.groups = [MagicMock(), MagicMock()]
        self.obstacle_sprites = MagicMock()
        self.create_attack = MagicMock()
        self.destroy_attack = MagicMock()
        self.create_magic = MagicMock()
        self.player = Player((0, 0), self.groups, self.obstacle_sprites, self.create_attack, self.destroy_attack, self.create_magic)

    def test_keyboard_input(self):
        # test pressing up arrow
        pygame = MagicMock()
        pygame.key.get_pressed = MagicMock(return_value={pygame.K_UP: True})
        self.player.keyboard_input()
        self.assertEqual(self.player.direction.y, -1)
        self.assertEqual(self.player.status, "up")

        # test pressing down arrow
        pygame.key.get_pressed = MagicMock(return_value={pygame.K_DOWN: True})
        self.player.keyboard_input()
        self.assertEqual(self.player.direction.y, 1)
        self.assertEqual(self.player.status, "down")

        # test pressing left arrow
        pygame.key.get_pressed = MagicMock(return_value={pygame.K_LEFT: True})
        self.player.keyboard_input()
        self.assertEqual(self.player.direction.x, -1)
        self.assertEqual(self.player.status, "left")

        # test pressing right arrow
        pygame.key.get_pressed = MagicMock(return_value={pygame.K_RIGHT: True})
        self.player.keyboard_input()
        self.assertEqual(self.player.direction.x, 1)
        self.assertEqual(self.player.status, "right")

        # test pressing space bar
        pygame.key.get_pressed = MagicMock(return_value={pygame.K_SPACE: True})
        self.player.create_attack = MagicMock()
        self.player.sword_attack_sound.play = MagicMock()
        self.player.keyboard_input()
        self.assertTrue(self.player.attacking)
        self.assertIsNotNone(self.player.attack_time)
        self.player.create_attack.assert_called_once()
        self.player.sword_attack_sound.play.assert_called_once()

        # test pressing left control
        pygame.key.get_pressed = MagicMock(return_value={pygame.K_LCTRL: True})
        self.player.create_magic = MagicMock()
        self.player.keyboard_input()
        self.assertTrue(self.player.attacking)
        self.assertIsNotNone(self.player.attack_time)
        self.player.create_magic.assert_called_once()

        # test pressing e
        pygame.key.get_pressed = MagicMock(return_value={pygame.K_e: True})
        self.player.can_switch_magic = True
        self.player.magic_index = 0
        self.player.magic = list(self.player.magic.keys())[self.player.magic_index]
        self.player.magic_switch_time = None
        self.player.keyboard_input()
        self.assertFalse(self.player.can_switch_magic)
        self.assertIsNotNone(self.player.magic_switch_time)
        self.assertEqual(self.player.magic_index, 1)
        self.assertEqual(self.player.magic, list(self.player.magic.keys())[self.player.magic_index])

if __name__ == "__main__":

    unittest.main()
