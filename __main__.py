from board import new_board, print_board
from actions import switch_player, is_winner, is_valid_move, make_move

board = new_board()
player1 = 'X'
player2 = 'O'
current_player = player1

while not is_winner(board, current_player):
    print_board(board)
    
    start = input(f"Player {current_player}, enter start position: ").upper()
    end = input(f"Player {current_player}, enter end position: ").upper()
    
    if is_valid_move(board, start, end):
        make_move(board, start, end, current_player)
        switch_player()
    else:
        print("That can't be done, try again.")

print_board(board)
print(f"Player {current_player} is so good, he just won by so much!")




   
