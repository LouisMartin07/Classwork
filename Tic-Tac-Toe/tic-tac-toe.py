# Step 1: Setting up the game board
def initialize_board():
    """Initializes the game board with empty spaces."""
    return [[" " for _ in range(3)] for _ in range(3)]

# Step 2: Displaying the game board
def display_board(board):
    """Displays the current state of the game board."""
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Step 3: Player Move
def player_move(board, row, col, symbol):
    """Allows the player to make a move on the board."""
    if board[row][col] == " ":
        board[row][col] = symbol
        return True
    else:
        return False

# Step 4: Computer Move - Starting with a simple random move for the computer
import random

def computer_move(board, symbol):
    """Computer makes a random move."""
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = symbol
            break




board = initialize_board()
        
# Step 5: Checking for Win or Tie
def check_win(board, symbol):
    """Checks if the given symbol has won the game."""
    # Check rows and columns
    for i in range(3):
        if all([board[i][j] == symbol for j in range(3)]) or all([board[j][i] == symbol for j in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == symbol for i in range(3)]) or all([board[i][2-i] == symbol for i in range(3)]):
        return True
    return False

def check_tie(board):
    """Checks if the game is a tie (no empty spaces left)."""
    for row in board:
        if " " in row:
            return False
    return True

# Step 6: Main Game Loop
# To make it more apparent when the computer is taking its turn, we can adjust the `main_game_with_spacing` function
# to display a message indicating the computer's move before showing the updated grid.

def main_game():
    board = initialize_board()
    player_symbol, computer_symbol = "X", "O"
    current_turn = "Player"
    
    while True:
        if current_turn == "Player":
            display_board(board)
            print("\n")  # Space before player's move for clarity
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if player_move(board, row, col, player_symbol):
                if check_win(board, player_symbol):
                    display_board(board)
                    print("Player wins!")
                    break
                current_turn = "Computer"
            else:
                print("Invalid move, try again.")
        else:
            # Message indicating the computer is making a move
            print("Computer is making its move...\n")
            computer_move(board, computer_symbol)
            if check_win(board, computer_symbol):
                display_board(board)
                print("Computer wins!")
                break
            current_turn = "Player"
            
            if check_tie(board):
                display_board(board)
                print("It's a tie!")
                break

        print("\n")  # Added space after moves for clarity

main_game()



