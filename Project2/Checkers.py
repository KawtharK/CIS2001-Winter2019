class Board:

    WHITE = 'W'
    BLACK = 'B'
    EMPTY = " "

    def __init__(self):
        self._board = []
        self.reset()
        self._max_jumps = 0
        self._current_jumps = 0

    def reset(self):
        self._board = []
        self._max_jumps = 0
        self._current_jumps = 0
        for row in range(8):
            self._board.append([])
            for column in range(8):
                self._board[row].append(self.EMPTY)

    def add_checker(self, who, row, col):
        self._board[row][col] = who

    def _count_jump(self):
        self._current_jumps += 1
        if self._current_jumps > self._max_jumps:
            self._max_jumps = self._current_jumps

    def _try_jump(self, row, col, row_adjust, col_adjust):
        if 0 <= row + row_adjust < len(self._board) and 0 <= col + col_adjust < len(self._board) \
                and self._board[row + ( row_adjust // 2 )][col + ( col_adjust // 2 ) ] == self.BLACK \
                and self._board[row + row_adjust][col + col_adjust] == self.EMPTY:
            self._count_jump()
            self._board[row + row_adjust // 2][col + col_adjust // 2] = self.EMPTY
            self._board[row + row_adjust][col + col_adjust] = self.WHITE
            self._board[row][col] = self.EMPTY
            self.num_jumps(row + row_adjust, col + col_adjust)
            self._board[row][col] = self.WHITE
            self._board[row + row_adjust][col + col_adjust] = self.EMPTY
            self._board[row + row_adjust // 2][col + col_adjust // 2] = self.BLACK
            self._current_jumps -= 1

    def num_jumps(self, row, col):
        if 0 <= row < len(self._board) and 0 <= col < len(self._board):

            # up left
            self._try_jump(row, col, -2, -2)

            # up right
            self._try_jump(row, col, -2, 2)

            # down right
            self._try_jump(row, col, 2, 2)

            # down left
            self._try_jump(row, col, 2, -2)
        return self._max_jumps

    def printme(self):
        for row in self._board:
            print(row)

