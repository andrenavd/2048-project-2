while not is_winner(board, current_player):
    print_board(board)
    
    start = input(f"Player {current_player}, enter start position: ").upper()
    end = input(f"Player {current_player}, enter end position: ").upper()
    
    if is_valid_move(board, start, end):
        make_move(board, start, end, current_player)
        current_player = switch_player(current_player, player1, player2)

          if len(position) == 2 and position[0] in 'ABCDEFGH' and position[1] in '12345678':
           
   
