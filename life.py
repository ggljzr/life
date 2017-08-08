import curses

# curses color pairs
PAIR_RED = 1
PAIR_GREEN = 2
PAIR_BLUE = 3
PAIR_YELLOW = 4
PAIR_CYAN = 5
PAIR_WHITE = 6
PAIR_BLACK = 7


class CursesGUI:

    def __init__(self):

        # init curses interface
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

    def startCurses(self):
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(1)
        curses.curs_set(0)  # no cursor

    def endCurses(self):
        # terminate curses application
        curses.nocbreak()
        curses.echo()
        self.stdscr.keypad(0)
        curses.endwin()

    def setPixel(self, y, x, color):
        self.stdscr.addch(y, x, curses.ACS_BLOCK,
                          curses.color_pair(color) | curses.A_BOLD)

    def refresh(self):
        self.stdscr.refresh()

if __name__ == '__main__':
    gui = CursesGUI()
    gui.startCurses()

    gui.setPixel(0,0, PAIR_GREEN)
    gui.setPixel(0, 1, PAIR_RED)
    while True:
        c = gui.stdscr.getch()
        if c == ord('q'):
            break


    gui.endCurses()
