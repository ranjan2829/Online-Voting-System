def reset():
    global board, counter
    board = [[0] * n for _ in range(n)]

def display(board):
    global counter
    counter += 1
    for row in board:
        print(" ".join(map(str, row)))
    print()

def check(board, row, column):
    for i in range(column):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n), range(column, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def marker(board, column):
    global counter
    possibility = False
    display(board)

    for i in range(n):
        if check(board, i, column):
            board[i][column] = 1
            possibility = marker(board, column + 1)
            board[i][column] = 0

    return possibility

n = int(input("Enter the size of the board: "))
counter = 0
reset()

if not marker(board, 0) and counter == 1:
    print("Feasible solution exists for the given dimensions")

print("There are a total of " + str(counter) + " possibilities for the given dimensions!")
