"""
File: battleship.py
Author: Ethan Holley
Purpose: A program that reads two files, and reads the position of 
        ships in a grid by player 1 and player 2 and responds based
        on the position guessed in the file. 
"""
import sys

class GridPos:
    """
    This class represents a grid as a two dimensional list. 
    The constructor method initalizes the grid at each position. 
    """
    def __init__(self, x, y, ship):
        self._x = x
        self._y = y
        self._ship = ship
        self._guess = 0
        self._health = 0

    def __str__(self):
        """
        This method returns a string version of the class.
        """
        if self._ship == None:
            return "N"
        else:
            return self._ship._type

class Board:
    """
    This class represents the 10 x 10 board with ship placements and 
    responds to the file based on the position of the ship. 
    The constructor initializes the board using a list and 
    grid as the distance. 
    """
    def __init__(self, ships_list, grid):
        self._ships_list = ships_list
        self._grid = grid 
    
    def process_guess(self, x, y):
        """
        This method is used for processing the guesses from 
        the inputed files. It checks if the position is already 
        taken or if ship is sunk. 
        Parameters:
            self - object itself
            x - int position from file
            y - int position from file
        Returns: None
        """
        if (x < 0 or y < 0 or x > 9 or y > 9):
            print("illegal guess")
        else:
            grid_position = self._grid[x][y]
            if grid_position._ship is None:
                if grid_position._guess != 0:
                    print("miss (again)")
                else:
                    print("miss")
                grid_position._guess = 1
            else:
                if grid_position._guess != 0:
                    print("hit (again)")
                else:
                    grid_position._ship._health -= 1
                    if grid_position._ship._health == 0:
                        print("{} sunk".format(grid_position._ship))
                    else:
                        print("hit")
                grid_position._guess = 1
                
class Ship:
    """
    This class represents the ships on the board. 
    The constructor initliazes the ship object. 
    """
    def __init__(self, list, details):
        self._details = details
        self._grid_position = []
        self._type = list[0]
        self._first_x = int(list[1])
        self._first_y = int(list[2])
        self._final_x = int(list[3])
        self._final_y = int(list[4])
        self.occupy_grid_position()
        self.valid_move()
    
    def __str__(self):
        return self._type
    
    def occupy_grid_position(self):
        """
        This method checks if the position of the ship is 
        already taken and the size of the various ships. 
        Parameters:
            self - object itself
        Returns: None
        """
        if self._first_x == self._final_x:
            self._size = abs(self._first_y - self._final_y) + 1
            self._health = abs(self._first_y - self._final_y) + 1

            for i in range(self._size):
                if self._first_y < self._final_y:
                    self._grid_position.append((self._first_x, \
                                                self._first_y + i))
                else:
                    self._grid_position.append((self._first_x, \
                                                self._first_y - i))
            
        elif self._first_y == self._final_y:
            self._size = abs(self._first_x - self._final_x) + 1
            self._health = abs(self._first_x - self._final_x) + 1

            for i in range(self._size):
                if self._first_x < self._final_x:
                    self._grid_position.append((self._first_x + i, \
                                                self._first_y))
                else:
                    self._grid_position.append((self._first_x - i, \
                                                self._first_y))
        else:
            print("ERROR: ship not horizontal or vertical: " + self._details)
            sys.exit(0)

    def valid_move(self):
        """
        This method checks if a move is valid or not based on 
        the kind of the ship with the given size. 
        Parameters:
            self - object itself
        Returns: None
        """
        if (self._type == "A" and self._size != 5) \
            or (self._type == "B" and self._size != 4) \
            or (self._type == "S" and self._size != 3) \
            or (self._type == "D" and self._size != 3) \
            or (self._type == "P" and self._size != 2):
            print("ERROR: incorrect ship size: " + self._details)
            sys.exit(0)

def read_file(placement, guess):
    """
    This function checks for input from the user which is processed
    as a ship object. It then calls the other classes to create the grid
    for and then checks the positions of the ships. It then processes
    the guess file and carries out the game of battleship with responses. 
    Parameters:
        placement - data from text file
        guess - guesses from text file
    Returns: None
    """
    ships_list = []
    grid = []
    for data in placement:
        details = data
        data = data.split()
        ship = Ship(data, details)
        for num in data[1:5]:
            if int(num) < 0 or int(num) > 9:
                print("ERROR: ship out-of-bounds: " + details)
                sys.exit(0)
        if ship not in ships_list:
            ships_list.append(ship)
        elif ship in ships_list:
            print("ERROR: fleet composition incorrect")
            sys.exit(0)
    
    if len(ships_list) != 5:
        print("ERROR: fleet composition incorrect")
        sys.exit(0)
    
    for i in range(10):
        columns = []
        for j in range(10):
            pos = None
            for ship in ships_list:
                if (i, j) in ship._grid_position:
                    if pos != None:
                        print("ERROR: overlapping ship: " + ship._details)
                        sys.exit(0)
                    pos = GridPos(i, j, ship)
            if pos == None:
                pos = GridPos(i, j, None)
            columns.append(pos)
        grid.append(columns)
    
    board = Board(ships_list, grid)
    for data in guess: 
        data = data.split()
        board.process_guess(int(data[0]), int(data[1]))
        ships_alive = 0
        for ship in board._ships_list:
            if ship._health != 0:
                ships_alive += 1
        if ships_alive == 0:
            print("all ships sunk: game over")
            sys.exit(0)

def main():
    """
    This function prompts the user for two files and calls the 
    read_file function to carry out the battleship game. 
    Parameters: None
    Returns: None
    """
    placement = open(input("Enter your placement file:\n")).readlines()
    guess = open(input("Enter your guess file:\n")).readlines()
    read_file(placement, guess)
main()

            
            



