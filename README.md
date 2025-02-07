# Sudoku Game

<p align="center">
  <img src="./sudoku.ico" alt="Sudoku Game" width="400" />
</p>

## Overview

This Sudoku game offers three different modes, incorporating AI-powered solving techniques such as **backtracking** and **arc consistency**. The game allows both human and AI interactions, making it an engaging and challenging experience for players.

## Features

- **Agent Challenge Mode**: The AI generates a random Sudoku board and solves it using **backtracking** and **arc consistency**.
- **Challenge Agent Mode**: The human player manually inputs a Sudoku board, challenging the AI to solve it.
- **User Challenge Mode**: The game generates Sudoku boards with different difficulty levels (**Easy, Medium, and Hard**) based on the number of empty tiles. The human player attempts to solve the board while the AI continuously checks for valid moves using **arc consistency**.

## Game Modes

### 1. Agent Challenge Mode

- The AI generates a random Sudoku board.
- The AI solves the board using **backtracking** and **arc consistency**.
- The solution is displayed to the user.

### 2. Challenge Agent Mode

- The human player manually creates a Sudoku board.
- The AI attempts to solve the user-generated board using **backtracking** and **arc consistency**.
- If the AI finds a solution, it is displayed; otherwise, it notifies the user that the board is unsolvable.

### 3. User Challenge Mode

- The AI generates a Sudoku board at the chosen difficulty level:
  - **Easy**: Few empty tiles.
  - **Medium**: Moderate number of empty tiles.
  - **Hard**: Many empty tiles.
- The human player attempts to solve the Sudoku board.
- AI checks each move to determine if it is valid using **arc consistency**.
- If the human makes an invalid move that leads to an unsolvable board, the AI alerts the player.

## How to Play

1. Select a game mode.
2. Follow on-screen instructions:
   - For **Agent Challenge Mode**, watch the AI solve the Sudoku.
   - For **Challenge Agent Mode**, input your custom board and challenge the AI.
   - For **User Challenge Mode**, select a difficulty and attempt to solve the puzzle.
3. In **User Challenge Mode**, each move will be validated by the AI.

## Technologies Used

- **Python programming language** for game logic and AI algorithms.

- **Tkinter library** for game GUI.

- **Backtracking algorithm** for Sudoku solving.

- **Arc Consistency (AC-3 Algorithm)** for constraint satisfaction and random board generation.

Enjoy solving Sudoku with AI assistance!

