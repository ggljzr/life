import curses
import numpy
import subprocess

from board import Board

if __name__ == '__main__':
    term_rows, term_cols = subprocess.check_output(['stty', 'size']).split()
    term_rows = int(term_rows)
    term_cols = int(term_cols)
    
    board = Board(term_rows, term_cols)
    board.start()
    board.gui.setPixel(0, 0, 7)

    while True:
        c = board.gui.stdscr.getch()
        if c == ord('q'):
            break


    board.end()
