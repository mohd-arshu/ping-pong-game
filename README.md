A simple two-player Pong game built with Python's turtle graphics
module.

Overview

This project recreates the classic Pong arcade game. Two players control
paddles on opposite sides of the screen and try to hit the ball past the
other player's paddle. The game tracks each player's score.

Features

Two-player paddle gameplay

Ball movement and wall bouncing

Paddle collision detection

Score tracking for both players

Simple graphics using Python's built-in turtle module

Requirements

Python 3

The turtle module (included with standard Python installations)

No third-party packages are required.

How to Run

Clone or download this repository.

Open a terminal in the project directory.

Run the main Python file. For example:

python main.py

Replace main.py with the actual filename if your game file has a
different name.

Controls

Use the keyboard controls configured in the game's paddle/listener code.
Check the main Python file for the exact keys assigned to each player's
paddle.

How the Game Works

The game loop repeatedly updates the screen and moves the ball.

When the ball reaches the top or bottom edge, its vertical direction
is reversed.

When the ball hits a paddle, its horizontal direction is reversed.

When the ball passes the right or left edge, it returns to the
centre and the appropriate player's score is increased.

Project Structure

pong-game/
├── main.py          # Starts the game and runs the game loop
├── ball.py          # Ball movement and bounce behaviour
├── paddle.py        # Paddle creation and movement
├── scoreboard.py    # Displays and updates the scores
└── README.md        # Project documentation

The filenames above are a suggested structure. Adjust them to match the
files in your repository.

Learning Outcomes

This project is useful for practising:

Python classes and object-oriented programming

Functions and methods

Loops and conditional statements

Object movement and collision detection

Basic event-driven keyboard controls

Future Improvements

Add a winning score and game-over screen

Add sound effects

Increase ball speed as the game progresses

Add a restart option

Created as a Python practice project.
