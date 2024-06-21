import math
import random
from board import get_valid_moves, check_win, make_move, player1, player2, empty_cell

import evaluators



def minimax_alpha_beta(board, depth, alpha, beta, maximizingPlayer, player, score_position_fun):
    valid_moves = get_valid_moves(board)
    is_terminal = check_win(board, player) or len(valid_moves) == 0
    opp_player = player1 if player == player2 else player1

    if depth == 0 or is_terminal:
        if is_terminal:
            if check_win(board, player):
                return (None, 100000000000000 if maximizingPlayer else -100000000000000)
            else:  # Remis
                return (None, 0)
        else:  # Głębokość = 0
            return (None, score_position_fun(board, player))

    if maximizingPlayer:
        value = -math.inf
        best_col = random.choice(valid_moves)
        for col in valid_moves:
            b_copy = [row[:] for row in board]
            make_move(b_copy, col, player)
            new_score = minimax_alpha_beta(b_copy, depth - 1, alpha, beta, False, player, score_position_fun)[1]
            new_score -= 100 #aby bardziej respektowac blizsze kroki
            if new_score > value:
                value = new_score
                best_col = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_col, value

    else:  # Minimalizujący gracz
        value = math.inf
        best_col = random.choice(valid_moves)
        for col in valid_moves:
            b_copy = [row[:] for row in board]
            make_move(b_copy, col, opp_player)
            new_score = minimax_alpha_beta(b_copy, depth - 1, alpha, beta, True, player, score_position_fun)[1]
            new_score -= 100  # aby bardziej respektowac blizsze kroki
            if new_score < value:
                value = new_score
                best_col = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_col, value





def ai_move(board, player, depth=4):
    column, minimax_score = minimax_alpha_beta(board, depth, -math.inf, math.inf, True, player, score_position_fun=evaluators.score_position)
    return column


