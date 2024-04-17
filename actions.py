player1 = 'X'  
player2 = 'O'  
current_player = player1  

def print_board(board):
    for row in board:
        print(' '.join(row))

def is_valid_move(start, end):
    pass

def make_move(start, end):
    pass

def switch_player():
    global current_player
    if current_player == player1:
        current_player = player2
    else:
        current_player = player1

def is_winner():
    pass
 
