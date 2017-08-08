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