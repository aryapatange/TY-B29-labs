# Tic-Tac-Toe using Minimax (X=Player, O=AI)

import math

# print board
def show(b):
    for i in range(0, 9, 3):
        print("|", b[i], b[i+1], b[i+2], "|")
    print()

# check winner
def winner(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for a,b1,c in wins:
        if board[a] == board[b1] == board[c] != " ":
            return board[a]
    return "Draw" if " " not in board else None

# minimax logic
def minimax(b, ai_turn):
    win = winner(b)
    if win == "O": return 1
    if win == "X": return -1
    if win == "Draw": return 0

    best = -math.inf if ai_turn else math.inf

    for i in range(9):
        if b[i] == " ":
            b[i] = "O" if ai_turn else "X"
            score = minimax(b, not ai_turn)
            b[i] = " "
            best = max(best, score) if ai_turn else min(best, score)

    return best

# choose best AI move
def best_move(b):
    best, move = -math.inf, None
    for i in range(9):
        if b[i] == " ":
            b[i] = "O"
            score = minimax(b, False)
            b[i] = " "
            if score > best:
                best, move = score, i
    return move

# game loop
board = [" "] * 9
print("You = X | AI = O\n")
show(board)

while True:
    # player move
    m = int(input("Move (0-8): "))
    if board[m] != " ": 
        print("Invalid!\n")
        continue
    board[m] = "X"
    show(board)
    if winner(board): break

    # ai move
    ai = best_move(board)
    board[ai] = "O"
    print("AI played:", ai)
    show(board)
    if winner(board): break

res = winner(board)
print("Result:", res)
