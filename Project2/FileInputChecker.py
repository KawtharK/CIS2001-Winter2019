import os
from Checkers import *


board = Board()

contents = os.listdir(r'C:\Users\EricC\Documents\GitHub\CIS2001-Winter2018\Project2')
for file in contents:
    os.path.isfile(file)
    if file.endswith(".txt"):
        print(file)
        with open(file) as current_file:
            for test_case in range(int(current_file.readline())):
                board.reset()
                first_white_row = -1
                first_white_col = -1
                white_pieces, black_pieces = current_file.readline().split()
                for white_piece in range(int(white_pieces)):
                    row, col = current_file.readline().split()
                    if first_white_row == -1:
                        first_white_row = int(row)
                        first_white_col = int(col)
                    board.add_checker(Board.WHITE, int(row), int(col))
                for black_pieces in range(int(black_pieces)):
                    row, col = current_file.readline().split()
                    board.add_checker(Board.BLACK, int(row), int(col))
                print("the number of jumps is", board.num_jumps(first_white_row, first_white_col))
                board.printme()

        print()


