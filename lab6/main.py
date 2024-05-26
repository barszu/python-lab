import random

height = 6
width = 7

board = [[' ' for x in range(width)] for y in range(height)]

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

def is_winner(board, player):
    # sprawdza wiersze
    for row in board:
        s = ''.join(row)
        if s.find(player * 4) >= 0:
            return True

    # sprawdza kolumny
    for col in range(width):
        for i in range(height - 3):
            if board[i][col] == board[i+1][col] == board[i+2][col] == board[i+3][col] == player:
                return True

    # sprawdza przekatne
    for i in range(height - 3):
        for j in range(width - 3):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == player:
                return True

    for i in range(3, height):
        for j in range(width - 3):
            if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3] == player:
                return True

    return False

def insert_to_column(board, col, player):
    for row in range(height-1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = player
            break
    return board

def ai_move(): #wykonuje ruch
    #wrzuca klocek do kolumny poprawnie aby wygrac
    # wrzuca na width sposobow
    while True:
        col = random.randint(0, width-1)
        if board[0][col] == ' ':
            break

    insert_to_column(board, col, 'O')
    return board

def ai_move_better():
    #generowac drzewko ruchow i wybierac najlepszy <- brute force
    return board

def my_move():
    while True:
        try:
            col = int(input("Podaj kolumne: ")) - 1
            if board[0][col] == ' ':
                break
        except:
            print("Podaj poprawna kolumne")

    insert_to_column(board, col, 'X')



# print(board_to_str(board))


def game_main():
    while True:
        print(board_to_str(board))
        my_move()
        if is_winner(board, 'X'):
            print("Wygrales!")
            break
        ai_move()
        if is_winner(board, 'O'):
            print("Przegrales!")
            break

game_main()