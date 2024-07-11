#Laboratuvar sorusundan farklı.
def print_sudoku(board):
    for row in board:
        print(" ".join(str(num) for num in row))

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)  # Satır ve sütun indexi
    return None

def is_valid(board, num, pos):
    # Satır kontrolü
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False


    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

            box_x = pos[1] // 3
            box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True  # Sudoku çözüldü
    else:
        row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_board):
    print_sudoku(sudoku_board)
else:
    print("Bu bulmaca çözülemez.")
