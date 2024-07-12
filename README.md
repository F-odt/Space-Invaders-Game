# Space Invaders

A simple implementation of the classic Space Invaders game using Python's Turtle graphics library.

## Description

This project is a basic version of Space Invaders, where the player controls a spaceship (represented by a green turtle) at the bottom of the screen. The objective is to shoot down alien ships (red circles) that are descending from the top of the screen while avoiding collisions with them.

## Features

- Player-controlled spaceship that moves left and right
- Ability to shoot lasers at alien ships
- Descending alien ships as obstacles
- Score tracking and high score display
- Game over condition when an alien collides with the player's ship

## Requirements

- Python 3.x
- Turtle graphics library (included in Python standard library)

## How to Run

1. Ensure you have Python installed on your system.
2. Save the game code in a file named `main_.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the `main_.py` file.
5. Run the following command: python main_.py

## Controls

- Left Arrow: Move the spaceship left
- Right Arrow: Move the spaceship right
- Spacebar: Shoot laser

## Game Rules

- The game starts with 5 alien ships.
- New alien ships appear when there are fewer than 5 on the screen.
- Each alien ship destroyed earns 10 points.
- The game ends when an alien ship collides with the player's spaceship.
- The high score is tracked across game sessions.

