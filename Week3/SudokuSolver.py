class SudokuPuzzle:
    EMPTY = " "

    def __init__(self):
        self.grid = []
        for row in range(9):
            self.grid.append([])
            for column in range(9):
                self.grid[row].append(SudokuPuzzle.EMPTY)

    def __str__(self):
        return "\n".join(str(row) for row in self.grid)

    def assign_number(self, row, col, number):
        if 0 <= row < 9 and 0 <= col < 9:
            if self.grid[row][col] != SudokuPuzzle.EMPTY:
                raise ValueError("This location is not empty")
            if self.can_place_number_in_position(row, col, number):
                self.grid[row][col] = number
            else:
                raise ValueError("You can't put that number there!")
        else:
            raise ValueError("Invalid row/col")

    def is_solved(self):
        for row in self.grid:
            if SudokuPuzzle.EMPTY in row:
                return False
        return True

    def can_place_number_in_position(self, row, col, number):
        if number in self.grid[row]:
            return False

        for puzzle_row in self.grid:
            if puzzle_row[col] == number:
                return False

        section_row = row // 3
        section_col = col // 3

        starting_row = section_row * 3
        starting_col = section_col * 3

        for row_to_check in range(starting_row, starting_row+3):
            for col_to_check in range(starting_col, starting_col+3):
                if self.grid[row_to_check][col_to_check] == number:
                    return False

        return True

    def solve(self):
        if not self.is_solved():
            row_index, col_index = self.find_first_empty_position()
            for number in range(1, 10):
                if self.can_place_number_in_position(row_index, col_index, number):
                    self.assign_number(row_index, col_index, number)
                    self.solve()
                    if not self.is_solved():
                        self.grid[row_index][col_index] = SudokuPuzzle.EMPTY

    def find_first_empty_position(self):
        for row_index in range(9):
            for col_index in range(9):
                if self.grid[row_index][col_index] == SudokuPuzzle.EMPTY:
                    return ( row_index, col_index )


empty_puzzle = SudokuPuzzle()
empty_puzzle.assign_number(0,0,3)
empty_puzzle.assign_number(1,0,2)
empty_puzzle.assign_number(3,0,8)
empty_puzzle.assign_number(5,0,7)
empty_puzzle.assign_number(7,0,9)
empty_puzzle.assign_number(8,0,6)
empty_puzzle.assign_number(0,3,8)
empty_puzzle.assign_number(0,5,1)
empty_puzzle.assign_number(0,8,2)




empty_puzzle.solve()
print(empty_puzzle)