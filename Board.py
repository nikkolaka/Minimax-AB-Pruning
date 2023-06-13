import numpy as np


# Node class for the tree
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    # checks if node is a leaf
    def is_leaf(self):
        return len(self.children) == 0


# Board class
class Board:
    def __init__(self, m, n):
        self.size = (n, m)
        self.board = np.array([["-"] * m] * n)
        self.last_move = None

    # creates children for the node
    def create_children(self, player):
        list = []
        for row in range(self.board.shape[0]):
            for col in range(self.board.shape[1]):
                if self.board[row][col] == "-":
                    child = Board(self.size[0], self.size[1])
                    child.board = self.board.copy()
                    child.set_square(col, row, player)
                    child.last_move = (col, row, player)
                    list.append(Node(child))
        return list

    def get_board(self):
        return self.board

    def get_size(self):
        return self.size

    def get_square(self, x, y):
        return self.board[y][x]

    # sets the square to the player shape
    def set_square(self, x, y, value):

        for i in range(y - 1, y + 2):
            for j in range(x - 1, x + 2):
                if i >= 0 and j >= 0 and i < self.board.shape[0] and j < self.board.shape[1]:
                    if self.board[i][j] == "-":
                        self.board[i][j] = "/"
        self.board[y][x] = value
        self.last_move = (x, y, value)

    # checks if the game is done
    def game_done(self):
        for row in self.board:
            for square in row:
                if square == "-":
                    return False
        return True

    # returns string of board
    def __str__(self):
        string = ""
        for row in self.board:
            string += str(row) + "\n"
        return str(string)

    # returns utility of board
    def get_utility(self):
        utility = 0
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                if self.board[i][j] == "-":
                    utility += 1
        return utility
