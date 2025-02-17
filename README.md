# battleship
This is a program that emulates the board game battleship. 

This program involves writing a program to model half of the actual board game, namely, Player 1's ship placements and Player 2's guesses.

The game setup. For the purposes of this program, the game board is a 10x10 grid. I use (x,y) coordinates to refer to the points of this grid: on each axis, grid values range from 0 through 9; the bottom-left corner has coordinates (0,0); and the top-right corner has coordinates (9,9).

Each player has five ships (one of each kind):
Ship Type      Abbr. Size
Aircraft carrier	A	  5
Battleship	      B	  4
Submarine	        S	  3
Destroyer	        D	  3
Patrol boat	      P	  2

Classes:
  GridPos - An instance of this class describes a grid position.
  Board - An instance of this class describes a board with a placement of ships.
  Ship - An instance of this class represents a ship.
