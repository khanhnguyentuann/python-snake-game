# Snake Game

## Introduction

This is a simple implementation of the classic Snake game in Python using the Pygame library.

## Features

- The game window has a grid for better visualization.
- The snake moves in a straight line and the player can change its direction using the arrow keys.
- The game ends if the snake hits the border or if it runs into itself.
- When the game ends, the final score is displayed and the player can start a new game by pressing the 'R' key.
- The game keeps track of the high score across all games, which is displayed in the game window.

## How to Run

1. Make sure you have Python and Pygame installed.
2. Download or clone this repository.
3. Navigate to the directory of the game files in the terminal.
4. Run the game by typing `python snake_game.py`.

## Code Details

- The game state is mainly managed in the `main` function. This includes the game loop, which listens for events, updates the game state, and renders the game window.
- The `game_over` function ends the current game, displays the final score, and allows the player to start a new game.
- The `draw_score` function displays the current score and high score in the game window.
- The `get_high_score` and `save_high_score` functions manage the high score.

## Dependencies

- Python 3
- Pygame
