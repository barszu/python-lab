from board import create_board, make_move, board_to_str, get_valid_moves, check_win, empty_cell, player1, player2
from ai import ai_move

board = create_board()

def my_move(board,player):
    while True:
        try:
            col = int(input("Podaj kolumne: ")) - 1
            if board[0][col] == empty_cell: break
        except:
            print("Podaj poprawna kolumne")

    return col

def game_with_AI(depth):
    while True:
        print(board_to_str(board))

        col = my_move(board, player1)
        make_move(board, col, player1)

        if check_win(board, player1):
            print("Wygrales!")
            break

        col = ai_move(board, player2, depth)
        make_move(board, col, player2)

        if check_win(board, player2):
            print("Przegrales!")
            break

if __name__ == '__main__':
    depth = 4
    game_with_AI(depth)

