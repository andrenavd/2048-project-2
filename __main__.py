class CheckersGame:
    def __init__(self):
        self.board = [
            [' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'],
            ['X', ' ', 'X', ' ', 'X', ' ', 'X', ' '],
            [' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['O', ' ', 'O', ' ', 'O', ' ', 'O', ' '],
            [' ', 'O', ' ', 'O', ' ', 'O', ' ', 'O'],
            ['O', ' ', 'O', ' ', 'O', ' ', 'O', ' '],
        ]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print(" ".join(row))

   
