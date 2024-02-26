def display_board(board):
  """
  Prints the current state of the Tic-Tac-Toe board.
  """
  for row in board:
    for cell in row:
      print(cell, end=" ")
    print()

def is_valid_move(board, row, col):
  """
  Checks if a move is valid (empty cell within board boundaries).
  """
  return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "

def has_won(board, symbol):
  """
  Checks if a player has won the game.
  """
  # Check rows and columns
  for i in range(3):
    if all(board[i][j] == symbol for j in range(3)) or \
       all(board[j][i] == symbol for j in range(3)):
      return True

  # Check diagonals
  return (board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol) or \
         (board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol)

def is_board_full(board):
  """
  Checks if all cells on the board are filled.
  """
  return all(cell != " " for row in board for cell in row)

def main():
  """
  Runs the Tic-Tac-Toe game.
  """
  board = [[" " for _ in range(3)] for _ in range(3)]
  current_player = "X"

  while True:
    display_board(board)

    # Get player move
    while True:
      row = int(input("Player " + current_player + ", enter row (1-3): ")) - 1
      col = int(input("Player " + current_player + ", enter column (1-3): ")) - 1
      if is_valid_move(board, row, col):
        break
      else:
        print("Invalid move. Please try again.")

    # Make the move
    board[row][col] = current_player

    # Check for winner or tie
    if has_won(board, current_player):
      display_board(board)
      print("Player " + current_player + " wins!")
      break
    elif is_board_full(board):
      display_board(board)
      print("It's a tie!")
      break

    # Switch player
    current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
  main()
