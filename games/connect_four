# Darius Corbin
# 03/15/2023
# Connect Four Game

print('Connect Four Game, By: Darius Corbin')


def print_board(board):
    for row in board:
        print('|', end='')
        for col in row:
            print(col, '|', end='')
        print()
    print('-' * (len(board[0]) * 2 - 1))


def check_win(board, col, player):
    # Check horizontal
    for i in range(len(board)):
        if board[i][col] != player:
            continue
        for j in range(max(0, col - 3), min(len(board[0]), col + 4)):
            if all(board[i][j + k] == player for k in range(4)):
                return True

    # Check vertical
    for j in range(col - 3, col + 1):
        if j < 0 or j >= len(board[0]):
            continue
        for i in range(len(board) - 3):
            if all(board[i + k][j] == player for k in range(4)):
                return True

    # Check diagonal (top-left to bottom-right)
    for i in range(len(board) - 3):
        for j in range(max(0, col - 3), min(len(board[0]), col + 4)):
            if all(board[i + k][j + k] == player for k in range(4)):
                return True

    # Check diagonal (bottom-left to top-right)
    for i in range(3, len(board)):
        for j in range(max(0, col - 3), min(len(board[0]), col + 4)):
            if all(board[i - k][j + k] == player for k in range(4)):
                return True

    return False


def play_game():
    board = [[' ' for _ in range(7)] for _ in range(6)]
    player = 1
    while True:
        print_board(board)
        col = input(f"Player {player}, choose a column (1-7): ")
        while not col.isdigit() or int(col) < 1 or int(col) > 7:
            col = input(f"Invalid input, player {player} choose a column (1-7): ")
        col = int(col) - 1

        for row in range(len(board) - 1, -1, -1):
            if board[row][col] == ' ':
                board[row][col] = 'X' if player == 1 else 'O'
                break
        else:
            print(f"Column {col + 1} is full, choose another column.")
            continue

        if check_win(board, col, 'X'):
            print_board(board)
            print("Player 1 wins!")
            break
        elif check_win(board, col, 'O'):
            print_board(board)
            print("Player 2 wins!")
            break

        player = 3 - player  # Alternate between player 1 and player 2

if __name__ == '__main__':
    play_game()
