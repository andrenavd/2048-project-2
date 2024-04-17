from board import new_board, print_board
from actions import switch_player, is_winner, is_valid_move, make_move

board = new_board()

while not is_winner():
    print_board(board)
    
    start = input(f"Player {current_player}, enter start position: ").upper()
    end = input(f"Player {current_player}, enter end position: ").upper()
    
    if is_valid_move(start, end):
        make_move(start, end)
        switch_player()
    else:
        print("That can´t be done, try again.")

print_board(board)
print(f"Player {current_player} is so good, he just won by so much!")



   
