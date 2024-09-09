# Conway's Game of Life Simulator
This repository contains a Python implementation of Conway's Game of Life, a cellular automaton devised by mathematician John Conway. The task is to build a class that can operate a session of Conway's Game of Life based on a provided interface. The implementation involves creating methods to manage the game board, update the game state, display results, and handle different starting configurations.

# Introduction
Conway's Game of Life is a zero-player game that consists of a grid of cells evolving through a series of iterations based on a set of rules. The game's complexity and beauty emerge from simple rules, creating various intricate patterns. It requires no input from a player after the initial setup, making it a fascinating study in emergent behavior.

# Overview
The primary objective of this project is to implement a class that simulates Conway's Game of Life. This class inherits properties from a interface (game_of_life_interface.py) and implements the necessary methods to manage and update the game's state according to rules.

# Files in the Repository
1) main.py: The main Python file containing the class implementation of Conway's Game of Life, which inherits from the interface.
2) game_of_life_interface.py: An interface file that outlines the structure and methods that the implementation must follow.

# Constructor and Initial Variables
The implemented class constructor can accept up to four parameters:
* size_of_board: An integer between 10 and 999 that defines the size of the game board.
* board_start_mode: An integer that defines the initial configuration of the board. If an unsupported integer is provided, board_start_mode=1 will be used by default.
* rle: A string representing a pattern in Run Length Encoding (RLE) format to be placed on the board. If provided, board_start_mode will be ignored.
* pattern_position: A tuple (x, y) representing the upper-left corner position of the initial pattern on the board. This is only used when rle is provided.
* rules: A string that defines the rules of the game. 

# Public Methods to Implement
The following methods are implemented in the class:
* update(): Updates the board state according to the rules of the game for one step.
* return_board(): Returns a two-dimensional list representing the current board state, where dead cells are denoted by 0 and alive cells are denoted by 255.
* save_board_to_file(file_name): Saves the current board state to a PNG file. The file_name parameter is a string specifying the desired file name (e.g., 1000.png). This method utilizes Matplotlib for visualization.
* display_board(): Displays the current board state on the screen using Matplotlib.
* transform_rle_to_matrix(rle): Converts an RLE string into a two-dimensional list representing the pattern, where 255 indicates a live cell.

# Board Start Modes
The board_start_mode parameter determines the initial configuration of the game board. The available modes are:
Mode 1: Random board where each cell has a 50% chance of being alive (np.random).
Mode 2: Random board where each cell has an 80% chance of being alive.
Mode 3: Random board where each cell has a 20% chance of being alive.
Mode 4: An empty board with a Gosper Glider Gun positioned at (10, 10).

# Run Length Encoding (RLE)
The rle parameter uses a text encoding format to specify patterns for the game board. Examples of RLE codes can be found at [ConwayLife Patterns](https://conwaylife.com/wiki/Category:Patterns).
Encoding format:
* b: Dead cell
* o: Live cell
* $: End of line
* 2 - 99: Represents counts of consecutive cells or lines
* !: End of the pattern
Example RLE patterns:
* Glider: bob$2bo$3o!
* C-heptomino: b3o$3ob$bo!

# Requirements
The following libraries are required to run the code:
* numpy
* matplotlib
