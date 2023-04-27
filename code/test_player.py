import pytest
from level import Level
from main import Game
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

main = Game()

def test_player_direction():
    assert main.level_one.player.status == 'down'

def test_player_specs():
    assert main.level_one.player.speed == 5
    assert main.level_one.player.attacking == False
    assert main.level_one.player.attack_cooldown == 400
    assert main.level_one.player.attack_time == None

def test_game_state():
    assert main.level_one.player.game_state == "start_menu"