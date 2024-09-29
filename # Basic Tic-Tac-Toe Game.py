# Basic Tic-Tac-Toe Game

# Description:
# This program allows two players to play Tic-Tac-Toe.

# How to Run:
# 1. Run the program.
# 2. Players take turns entering their moves.
# 3. The program will announce the winner or a tie.

# The code:

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Initialize the game board
board = [[" " for _ in range(3)] for _ in range(3)]
turn = "X"

for _ in range(9):
    print_board(board)
    row = int(input(f"Player {turn}, enter the row (0-2): "))
    col = int(input(f"Player {turn}, enter the column (0-2): "))

    if board[row][col] == " ":
        board[row][col] = turn
        if any(all(cell == turn for cell in row) for row in board) or \
           any(all(board[r][c] == turn for r in range(3)) for c in range(3)) or \
           all(board[i][i] == turn for i in range(3)) or \
           all(board[i][2 - i] == turn for i in range(3)):
            print_board(board)
            print(f"Player {turn} wins!")
            break
        turn = "O" if turn == "X" else "X"
    else:
        print("Invalid move! Try again.")
else:
    print("It's a tie!")
