height = 6
width = 7

empty_cell = ' '
player1 = 'X'
player2 = 'O'

def create_board():
    return [[empty_cell for x in range(width)] for y in range(height)]

def make_move(board, col, player):
    for row in reversed(range(len(board))):
        if board[row][col] == empty_cell:
            board[row][col] = player
            return
    else:
        raise ValueError('Column is full')

def board_to_str(board):
    res = ''
    # res += '-' * (width * 2 + 1) + '\n'
    for row in board:
        res += '|'
        for col in row:
            res += col + '|'
        res += '\n'
        # res += '-' * (width * 2 + 1) + '\n'
    return res

def get_valid_moves(board):
    valid_moves = []
    for col in range(len(board[0])):
        if board[0][col] == empty_cell:
            valid_moves.append(col)
    return valid_moves


def check_win(board, player):
    # Sprawdzanie poziomów
    for row in range(len(board)):
        for col in range(len(board[0]) - 3):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    # Sprawdzanie pionów
    for col in range(len(board[0])):
        for row in range(len(board) - 3):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    # Sprawdzanie ukośnych (góra-lewo do dół-prawo)
    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

    # Sprawdzanie ukośnych (góra-prawo do dół-lewo)
    for row in range(3, len(board)):
        for col in range(len(board[0]) - 3):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True

    return False

