import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_SIZE = 300
CELL_SIZE = SCREEN_SIZE // 3
WIN_LINE_WIDTH = 15
SCREEN = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Tic Tac Toe")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Game variables
board = [[" " for _ in range(3)] for _ in range(3)]
player_turn = True  # True for player's turn, False for computer's turn

def draw_board():
    SCREEN.fill(WHITE)
    for i in range(1, 3):
        pygame.draw.line(SCREEN, BLACK, (0, i * CELL_SIZE), (SCREEN_SIZE, i * CELL_SIZE), 3)
        pygame.draw.line(SCREEN, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, SCREEN_SIZE), 3)

def draw_moves():
    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                pygame.draw.line(SCREEN, BLACK, (col * CELL_SIZE + 20, row * CELL_SIZE + 20),
                                 ((col + 1) * CELL_SIZE - 20, (row + 1) * CELL_SIZE - 20), WIN_LINE_WIDTH)
                pygame.draw.line(SCREEN, BLACK, ((col + 1) * CELL_SIZE - 20, row * CELL_SIZE + 20),
                                 (col * CELL_SIZE + 20, (row + 1) * CELL_SIZE - 20), WIN_LINE_WIDTH)
            elif board[row][col] == "O":
                pygame.draw.circle(SCREEN, RED, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2),
                                   CELL_SIZE // 2 - 20, WIN_LINE_WIDTH)

def player_move(x, y):
    global player_turn
    row = y // CELL_SIZE
    col = x // CELL_SIZE
    if board[row][col] == " ":
        board[row][col] = "X"
        player_turn = False

def computer_move():
    global player_turn
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "O"
        player_turn = True

def check_win(symbol):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)) or all(board[j][i] == symbol for i in range(3)):
            return True
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2-i] == symbol for i in range(3)):
        return True
    return False

def check_tie():
    for row in board:
        if " " in row:
            return False
    return True

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and player_turn:
            x, y = pygame.mouse.get_pos()
            player_move(x, y)
            if check_win("X"):
                print("Player wins!")
                running = False
            elif check_tie():
                print("It's a tie!")
                running = False

    if not player_turn and not running:
        computer_move()
        if check_win("O"):
            print("Computer wins!")
            running = False
        elif check_tie():
            print("It's a tie!")
            running = False
        player_turn = True

    draw_board()
    draw_moves()
    pygame.display.flip()

pygame.quit()
sys.exit()

