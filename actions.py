player1 = 'X'
player2 = 'O'
current_player = player1

def print_board(board):
    for row in board:
        print(' '.join(row))

def is_valid_move(board, start, end):
    pass

def make_move(board, start, end, player):
    pass

def switch_player():
    global current_player
    if current_player == player1:
        current_player = player2
    else:
        current_player = player1

def is_winner(board, player):
    pass

