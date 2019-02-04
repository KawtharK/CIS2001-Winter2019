class KnightsTour:

    EMPTY = ' '
    JUMPS = ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2))

    def __init__(self, size):
        self.board = []
        self.is_solved = False
        for row in range(size):
            self.board.append([])
            for column in range(size):
                self.board[row].append( KnightsTour.EMPTY )
        self.current = 0
        self._solve(0,0)

    def is_valid_open_space(self, row, col):
        if row < 0 or row >= len(self.board):
            return False
        if col < 0 or col >= len(self.board):
            return False
        return self.board[row][col] == KnightsTour.EMPTY

    def _solve(self, row, col):
        #print(self.current)
        self.current += 1
        self.board[row][col] = self.current

        if self.current == len(self.board)**2:
            self.is_solved = True
            return

        positions = [ Position(self, row+jump[0], col+jump[1]) for jump in KnightsTour.JUMPS if self.is_valid_open_space(row+jump[0], col+jump[1]) ]

        # same as above
        #positions = []
        #for jump in KnightsTour.JUMPS:
        #    if self.is_valid_open_space(row+jump[0], col+jump[1]):
        #        positions.append( Position(self, row+jump[0], col+jump[1]))

        positions.sort()
        for position in positions:
            if not self.is_solved:
                self._solve(position.row, position.col)
                if not self.is_solved:
                    self.board[position.row][position.col] = KnightsTour.EMPTY
                    self.current -= 1

    def __str__(self):
        return '\n'.join(str(row) for row in self.board)


class Position:

    def __init__(self, knights_tour, row, col):
        self.knights_tour = knights_tour
        self.row = row
        self.col = col

    def valid_moves(self):
        moves = 0
        for jump in KnightsTour.JUMPS:
            if self.knights_tour.is_valid_open_space(self.row+jump[0], self.col+jump[1]):
                moves += 1
        return moves

    def __lt__(self, other):
        return self.valid_moves() < other.valid_moves()

    def __gt__(self, other):
        return self.valid_moves() > other.valid_moves()

    def __eq__(self, other):
        return self.valid_moves() == other.valid_moves()


knights_tour = KnightsTour(8)
print(knights_tour)



