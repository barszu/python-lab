from board import empty_cell, player1, player2
import re


def get_all_diagonals(matrix, min_length=4):
    rows = len(matrix)
    cols = len(matrix[0])

    # Listy do przechowywania przekątnych
    diagonals = []

    # Przekątne od lewej do prawej (włącznie z główną przekątną)
    for start_col in range(cols):
        diagonal = []
        for r, c in zip(range(rows), range(start_col, cols)):
            diagonal.append(matrix[r][c])
        if len(diagonal) >= min_length:
            diagonals.append(diagonal)

    for start_row in range(1, rows):
        diagonal = []
        for r, c in zip(range(start_row, rows), range(cols)):
            diagonal.append(matrix[r][c])
        if len(diagonal) >= min_length:
            diagonals.append(diagonal)

    # Przekątne od prawej do lewej (włącznie z główną przekątną)
    for start_col in range(cols):
        diagonal = []
        for r, c in zip(range(rows), range(start_col, -1, -1)):
            diagonal.append(matrix[r][c])
        if len(diagonal) >= min_length:
            diagonals.append(diagonal)

    for start_row in range(1, rows):
        diagonal = []
        for r, c in zip(range(start_row, rows), range(cols - 1, -1, -1)):
            diagonal.append(matrix[r][c])
        if len(diagonal) >= min_length:
            diagonals.append(diagonal)

    return diagonals

def build_pattern(pattern):
    return fr"(?=({pattern}))"

def find_patterns_no(window, pattern):
    return len(re.findall(pattern, window))

def find_matches_score(window:str, regex, weight, player: str):
    # regex only with A B
    pattern = regex.replace('0', empty_cell).replace('A', player)
    pattern = build_pattern(pattern)
    matches_no = find_patterns_no(window, pattern)
    score = weight * matches_no
    return score


def evaluate_window(window, player: str):
    score = 0
    opp_player = player1 if player == player2 else player1

    window = ''.join(window)

    # Idealny przypadek - 4 pionki gracza w oknie
    regex = 'AAAA'
    weight = 10000
    score += find_matches_score(window, regex, weight*100, player)
    score -= find_matches_score(window, regex, weight, opp_player)

    # Dobra sytuacja - 3 pionki gracza i 1 puste miejsce
    regex = 'AAA0|AA0A|A0AA|0AAA'
    weight = 10
    score += find_matches_score(window, regex, weight*3, player)
    score -= find_matches_score(window, regex, weight+3, opp_player)

    # Akceptowalna sytuacja - 2 pionki gracza i 2 puste miejsca
    regex = 'AA00|A0A0|A00A|0AA0|0A0A|00AA'
    weight = 5
    score += find_matches_score(window, regex, weight, player)
    score -= find_matches_score(window, regex, weight+3, opp_player)

    return score


def score_position(board, player):
    score = 0
    row_count = len(board)
    col_count = len(board[0])

    # Definiowanie wag dla poziomów
    level_weights = [i for i in range(row_count)]

    # Sprawdzanie środka planszy (ważniejsze miejsca)
    center_array = [board[i][col_count // 2] for i in range(row_count)]
    score += evaluate_window(center_array, player) * 6

    # Sprawdzanie poziomów
    for row in range(row_count):
        window = board[row]
        score += evaluate_window(window, player)

    # Sprawdzanie pionów
    for col in range(col_count):
        window = [board[i][col] for i in range(row_count)]
        score += evaluate_window(window, player)

    #przekatne
    for window in get_all_diagonals(board):
        score += evaluate_window(window, player)

    return score