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

def test_spawn_interval():
    assert main.spawn_interval == 3000

def test_user_text():
    assert len(main.user_text) == 0

def test_get_top_five_scores():
    top_scores = main.get_top_five_scores()
    assert len(top_scores) == 5