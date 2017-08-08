import curses
from abc import ABC, abstractmethod

# curses color pairs
PAIR_RED = 1
PAIR_GREEN = 2
PAIR_BLUE = 3
PAIR_YELLOW = 4
PAIR_CYAN = 5
PAIR_WHITE = 6
PAIR_BLACK = 7


class GUI(ABC):

    @abstractmethod
    def setPixel(self, row, col, color):
        pass

    @abstractmethod
    def drawBoard(self, board):
        pass

    @abstractmethod
    def startGui(self):
        pass

    @abstractmethod
    def endGui(self):
        pass


class CursesGUI(GUI):

    def setPixel(self, row, col, color):
        try:
            self.stdscr.addch(row, col, curses.ACS_BLOCK,
                              curses.color_pair(color) | curses.A_BOLD)
        except curses.error as e:
            #print("setPixel error")
            # print(e)
            pass

    def drawBoard(self, board):
        for row in range(0, board.shape[0]):
            for col in range(0, board.shape[1]):
                if board[row][col] == 0:
                    self.setPixel(row, col, PAIR_BLACK)
                else:
                    self.setPixel(row, col, PAIR_GREEN)
        self.refresh()

    def __init__(self):

        # init curses interface1
        self.stdscr = curses.initscr()

        # colors
        curses.start_color()
        curses.init_pair(PAIR_RED, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(PAIR_GREEN, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(PAIR_BLUE, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(PAIR_YELLOW, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(PAIR_CYAN, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(PAIR_WHITE, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(PAIR_BLACK, curses.COLOR_BLACK, curses.COLOR_BLACK)

    def startGui(self):
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(1)
        curses.curs_set(0)  # no cursor

    def endGui(self):
        # terminate curses application
        curses.nocbreak()
        curses.echo()
        self.stdscr.keypad(0)
        curses.endwin()

    def refresh(self):
        self.stdscr.refresh()
