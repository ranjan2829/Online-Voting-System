def print_board(board):
    print("Current State Of Board:\n")
    for i in range(9):
        if (i > 0) and (i % 3 == 0):
            print("\n")
        if board[i] == 0:
            print("- ", end=" ")
        elif board[i] == 1:
            print("O ", end=" ")
        elif board[i] == -1:
            print("X ", end=" ")
    print("\n\n")

def user_turn(player, board):
    pos = int(input(f"Enter {player}'s position from [1...9]: "))
    if board[pos - 1] != 0:
        print("Wrong Move!!!")
        exit(0)
    board[pos - 1] = -1 if player == 'X' else 1

def minimax(board, player):
    x = analyze_board(board)
    if x != 0:
        return x * player, -1

    pos, value = -1, -2
    for i in range(9):
        if board[i] == 0:
            board[i] = player
            score, _ = minimax(board, player * -1)
            board[i] = 0

            if score > value:
                value = score
                pos = i

    if pos == -1:
        return 0, -1
    return value, pos

def comp_turn(board):
    score, pos = minimax(board, 1)
    board[pos] = 1

def analyze_board(board):
    cb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in range(8):
        if board[cb[i][0]] != 0 and board[cb[i][0]] == board[cb[i][1]] == board[cb[i][2]]:
            return board[cb[i][2]]
    return 0

def main():
    print("Computer : O Vs. You : X")
    player = int(input("Enter to play 1(st) or 2(nd): "))
    board = [0] * 9

    for i in range(9):
        if analyze_board(board) != 0:
            break
        if (i + player) % 2 == 0:
            comp_turn(board)
        else:
            print_board(board)
            user_turn('X', board)

    x = analyze_board(board)
    if x == 0:
        print_board(board)
        print("Draw!!!")
    elif x == -1:
        print_board(board)
        print("X Wins!!! O Loses!!!")
    elif x == 1:
        print_board(board)
        print("X Loses!!! O Wins!!!")

if __name__ == "__main__":
    main()
