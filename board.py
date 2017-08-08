from time import sleep
from gui import CursesGUI
import numpy as np



class Board:

    def __init__(self, rows, cols):
        self.gui = CursesGUI()
        self.rows = rows
        self.rows = cols
        self.board = np.random.randint(2, size=(rows, cols))
    def start(self):
        self.gui.startGui()
        self.gui.drawBoard(self.board)

    def end(self):
        self.gui.endGui()

    def step(self):
        newBoard = np.zeros(self.board.shape, dtype=int)

        for row in range(0, self.board.shape[0]):
            for col in range(0, self.board.shape[1]):
                d = 1
                neigbours = self.board[row-d:row+d+1, col-d:col+d+1]
                neigbours = neigbours.flatten().sum() - self.board[row][col]

                if neigbours < 2 or neigbours > 3:
                    newBoard[row][col] = 0
                elif neigbours == 3:
                    newBoard[row][col] = 1
                else:
                    newBoard[row][col] = self.board[row][col]

        self.board = newBoard
        self.gui.drawBoard(self.board)
        #sleep(1)
