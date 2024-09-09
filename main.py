import game_of_life_interface

import numpy as np
import matplotlib.pyplot as plt


class GameOfLife(game_of_life_interface.GameOfLife):  # This is the way you construct a class that inherits properties
    def __init__(self, size_of_board, board_start_mode, rules, rle='', pattern_position=(0, 0)):
        """ init method for class GameOfLife. Input size_of_board donates the size of the board, is an integer bigger
        than 9 and smaller than 1000. board_start_mode donates the starting position options, please refer to the
        added PDF file. Is an integer. rules donates the rules of the game. Is a string rle: is a str[optional]. the
        coding for a pattern, if there is an rle coding than the board_start_mode is overlooked, if there isn't an
        rle, than use the board_start_mode. pattern_position: is a tuple of two integers (x,y). the upper left
        position of the pattern on the board, only used if in rle mode. Output None.
        """
        self.size_of_board = size_of_board
        self.board_start_mode = board_start_mode
        self.rules = rules
        self.rle = rle
        self.pattern_position = pattern_position
        self.dead = 0
        self.alive = 255
        self.board = self.create_a_board()

    def create_a_board(self):
        """ This method returns a list that encodes the board: The board is a two dimensional
        list that every cell denotes if the cell is “dead” or “alive” based on the choice of the board start mode.
        Input None.
        Output new board.
        """
        if self.rle == "":  # if rle is an empty string, the board_start_mode should not be ignored.
            if self.board_start_mode == 2:
                # Each cell is `alive’ with probability 0.8
                return np.random.choice([self.dead, self.alive], self.size_of_board * self.size_of_board,
                                        p=[0.2, 0.8]).reshape(self.size_of_board, self.size_of_board)
            if self.board_start_mode == 3:
                # Each cell is `alive’ with probability 0.2
                return np.random.choice([self.dead, self.alive], self.size_of_board * self.size_of_board,
                                        p=[0.8, 0.2]).reshape(self.size_of_board, self.size_of_board)
            if self.board_start_mode == 4:
                # the board start empty with a Gosper Glider Gun in top left cell at (10, 10).
                self.pattern_position = (10, 10)
                return self.trans_rle_to_matrix(
                    "24bo$22bobo$12b2o6b2o12b2o$11bo3bo4b2o12b2o$2o8bo5bo3b2o$2o8bo3bob2o4bobo$10bo5bo7bo$11bo3bo$12b2o!")
            else:
                # if a different integer is provided, board_start_mode=1 should be chosen which mean that each
                # cell is `alive’ with probability 0.5
                return np.random.choice([self.dead, self.alive], self.size_of_board * self.size_of_board,
                                        p=[0.5, 0.5]).reshape(self.size_of_board, self.size_of_board)
        else:
            return self.trans_rle_to_matrix(self.rle)

    def update(self):
        """ This method updates the board game by the rules of the game. Do a single iteration.
        Input None.
        Output None.
        """
        duplicate_board = self.board.copy()  # copy board so the method updates the board for one step.
        size = self.size_of_board
        board = self.board
        new_gen, survivor = self.rules_reader()
        for i in range(size):
            for j in range(size):
                # calculate the value of cell (i, j) based on its neighbors, taking into account the boundary
                # conditions.
                total = int((board[i, (j - 1) % size] + board[i, (j + 1) % size] +
                             board[(i - 1) % size, j] + board[(i + 1) % size, j] +
                             board[(i - 1) % size, (j - 1) % size] + board[(i - 1) % size, (j + 1) % size] +
                             board[(i + 1) % size, (j - 1) % size] + board[(i + 1) % size, (j + 1) % size]) / self.alive)
                # apply rules of the game while using the method rules_reader
                if self.board[i][j] == self.dead:
                    if str(total) in new_gen:  # check if has exactly three neighbors that are alive
                        duplicate_board[i][j] = self.alive
                else:  # if a cell is alive
                    if str(total) in survivor:  # check if has either two or three neighbors that are alive
                        pass  # it remains alive
                    else:  # if has fewer than two neighbors that are alive or has more than three neighbors that are
                        # alive
                        duplicate_board[i][j] = self.dead 
        self.board = duplicate_board  # update the old board

    def save_board_to_file(self, file_name):
        """ This method saves the current state of the game to a file. You should use Matplotlib for this.
        Input img_name donates the file name. Is a string, for example file_name = '1000.png'
        Output a file with the name that donates filename.
        """
        plt.imsave(file_name, self.board)

    def display_board(self):
        """ This method displays the current state of the game to the screen. You can use Matplotlib for this.
        Input None.
        Output a figure should be opened and display the board.
        """
        plt.imshow(self.board)
        plt.show()

    def return_board(self):
        """ This method returns a list of the board position. The board is a two-dimensional list that every
        cell donates if the cell is dead or alive. Dead will be donated with 0 while alive will be donated with 255.
        Input None.
        Output a list that holds the board with a size of size_of_board*size_of_board.
        """
        return self.board.tolist()

    def transform_rle_to_matrix(self, rle):
        """ This method transforms an rle coded pattern to a two dimensional list that holds the pattern,
         Dead will be donated with 0 while alive will be donated with 255.
        Input an rle coded string.
        Output a two dimensional list that holds a pattern with a size of the bounding box of the pattern.
        """
        list_of_lists = []
        list_by_rle = []
        index = 0
        char = rle[index]
        while char in rle:
            if char == "b":
                list_by_rle.append(self.dead)
                index += 1
                char = rle[index]
            elif char == "o":
                list_by_rle.append(self.alive)
                index += 1
                char = rle[index]
            elif char == "$":
                list_of_lists.append(list_by_rle)
                list_by_rle = []
                index += 1
                char = rle[index]
            elif char.isdigit():
                if rle[index + 1].isdigit():
                    num = int(char) * 10 + int(rle[index + 1])
                    index += 2
                    char = rle[index]
                else:
                    num = int(char)
                    index += 1
                    char = rle[index]
                if char == "b":
                    for char in range(num):
                        list_by_rle.append(self.dead)
                    index += 1
                    char = rle[index]
                elif char == "o":
                    for char in range(num):
                        list_by_rle.append(self.alive)
                    index += 1
                    char = rle[index]
                elif char == "$":
                    list_of_lists.append(list_by_rle)
                    list_by_rle = []
                    for i in range(num - 1):
                        list_of_lists.append([0] * len(list_of_lists[0]))
                    index += 1
                    char = rle[index]
            if char == "!":
                list_of_lists.append(list_by_rle)
                break
        if len(list_of_lists[-1]) < len(list_of_lists[0]):
            for char in range(len(list_of_lists[0]) - len(list_of_lists[-1])):
                list_of_lists[-1].append(self.dead)
        return list_of_lists

    def trans_rle_to_matrix(self, rle):
        # based on the examples in the PDF file: bob$2bo$3o! , b3o$3ob$bo!
        board_by_rle = np.zeros((self.size_of_board, self.size_of_board), int)
        index = 0
        char = rle[index]
        row = int(self.pattern_position[0])
        column = int(self.pattern_position[1])
        while char != "!":  # as long as this is not the end of pattern
            if char == "b":  # Dead cell
                column += 1  # moving on
            elif char == "o":  # Live cell
                board_by_rle[row][column] = self.alive  # brings back to life
                column += 1  # next step
            elif char == "$":  # End of line
                row += 1  # next line
                column = self.pattern_position[1]  # column start
            elif (char >= "1") and (char <= "9"):  # if single digit
                if (rle[index + 1] >= "0") and (rle[index + 1] <= "9"):
                    if rle[index + 2] == "$":  # if we've reached to the end of the line in the next 2 spots
                        row += int(char + rle[index + 1])  # next line
                        column = self.pattern_position[1]  # column start
                    elif rle[index + 2] == "b":
                        column += int(
                            char + rle[index + 1])  # advanced in spots according to the number typed before b
                    else:  # if live cell
                        for i in range(int(char + rle[index + 1])):
                            board_by_rle[row][
                                column] = self.alive  # brings several cells to life according to the number entered
                            column += 1  # next spot
                    index += 2
                else:
                    if rle[index + 1] == "$":
                        row += int(char)  # next line
                        column = self.pattern_position[1]  # first column
                    elif rle[index + 1] == "b":
                        column += int(char)  # skip column based on the number entered
                    else:  # if live cell
                        for i in range(int(char)):
                            board_by_rle[row][column] = self.alive
                            column += 1
                    index += 1
            index += 1
            char = rle[index]
        return board_by_rle

    def rules_reader(self):
        """ This method checks a string that holds the rules of the game and follows the rules if an alive cell is
        survive or a dead cell is reborn into a new generation.
        Input None.
        Output encoded rule.
        """
        index = 1
        R = ""
        rule = self.rules[index]
        while rule != "/":
            R += rule
            index += 1
            rule = self.rules[index]
        new_gen = R
        R = ""
        index += 2
        for i in range(index, len(self.rules)):
            rule = self.rules[i]
            R += rule
        survivor = R
        return new_gen, survivor


if __name__ == '__main__':  # You should keep this line for our auto-grading code.
    print('write your tests here')  # don't forget to indent your code here!