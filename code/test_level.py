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

def test_level_pause():
    assert main.level_one.pause == False

def test_current_attack():
    assert main.level_one.pause == False

def test_enemy_list():
    assert main.level_one.enemy_list ==  ["bamboo", "spirit", "raccoon", "squid"]

def test_enemies_number():
    assert len(main.level_one.enemies) == 0