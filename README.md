### Software Engineering Project
# The Battle For Sugar Rush
## A 2D Zelda Style Game

### Victor Ekpenyong, Dallas Gere, Sam Randall

## Overview
- This repository holds our all the files needed to run our game made using python's pygame. You can also find the class diagram made using pycharm showing how each class and methods interact with each other as well as our original Project Proposal and Software Requirements Specificatioins (SRS). Unit Testing on some basic class variables and methods was implemented using pytest.

## Initial Set Up
1. Make sure you have pygame
   - 'pip install pygame'
2. In order to run pytest unit tests, make sure you have pytest
   - 'pip install pytest'

## How to start the game
1. Open your terminal/command line and go into the SWE-Project directory
2. navigate into the 'code' directory
   - current director should look like : SWE-Project\code
3. To start the game run
   - python main.py
4. If that did not work, try
   - python3 main.py
4. Play the game and Enjoy

## How to run Unit Tests
1. Open your terminal/command line and go into the SWE-Project directory
2. navigate into the 'code' directory
   - current director should look like : SWE-Project\code
3. To run all unit tests type within your terminal / command line
   - pytest
4. To run a specific unit test, try
   - pytest <file_name>

## Special Implementations
* A Leaderboard is shown within the game which reads information from a text file within a game and also allows the user to save their score to the leaderboard. The top 5 scores and names are shown within the game
* Pausing and Resuming the game is implemented as we as the ability to quit the game and go back to the start screen once paused
* Multiple sounds and music has been added to improve game experience including a music shift once the players health gets low

## Enjoy Our Game!
