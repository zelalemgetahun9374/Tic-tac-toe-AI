class TicTacToe():
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.winner = None

    @staticmethod
    def print_num_board():
        print("Game board move map\n")
        nums = [[str(j + i * 3) for j in range(3)] for i in range(3)]

        for row in nums:
            print(f"| {' | '.join(row)} |")
        print("")

    def print_board(self):
        rows = [self.board[i * 3: (i + 1) * 3] for i in range(3)]

        for row in rows:
            print(f"| {' | '.join(row)} |")

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def num_empty_squares(self):
        return self.board.count(' ')

    def game_won(self, square, letter):
        row_idx = square // 3  # row index
        row = self.board[row_idx * 3: (row_idx + 1) * 3]

        if all(letter == i for i in row):
            return True

        col_idx = square % 3  # column index
        column = [self.board[col_idx + i * 3] for i in range(3)]
        if all(letter == i for i in column):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            diagonal2 = [self.board[i] for i in [2, 4, 6]]

            if all(letter == i for i in diagonal1) or all(letter == i for i in diagonal2):
                return True

        return False

    def make_move(self, square, letter):
        self.board[square] = letter
        if self.game_won(square,letter):
            self.winner = letter
