from tabulate import tabulate

board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]


def draw_board(board):
    print("-" * 33)
    for i in range(9):
        for j in range(9):
            if j == 2 or j == 5:
                print(board[i][j], end=" ║ ")
            elif j!= 8:
                print(board[i][j], end=" | ")
            else:
                print(board[i][j], end="")
        print()
        if i == 2 or i == 5:
            print("="*33)
        else:
            print("-"*33)

def get_empty_positions(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return [i, j]
    return None

def valid(row, col, num, board):

    # check the whole grid
    for i in range(9):
        if board[row][i] == num:
            return False
        if board[i][col] == num:
            return False
    
    # check sub grid
    col_start = (col // 3) * 3 
    row_start = (row // 3) * 3

    for i in range(3):
        for j in range(3):
            if board[row_start + i][col_start + j] == num:
                return False
    return True

def solve(board):
    # define base case -> board is full
    empty = get_empty_positions(board)
    if not empty:
        return True # splution find -> full board
    else:
        row, col = empty

    for i in range(1, 9+1):
        if valid(row, col, i, board):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0
    
    return False

if solve(board):
    draw_board(board)
else:
    print("No solution!")