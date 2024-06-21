from src.suplementaries.global_const import *


def check_syntax(exp: str):
    state = True #oczekuje na litere
    bracket_cnt = 0
    for letter in exp:
        if letter == '~': continue
        if state:
            if letter == OPEN_BRACKET:
                bracket_cnt += 1
            elif letter in LITERAL:
                state = False
            else:
                return False
        else:
            if letter == CLOSE_BRACKET:
                bracket_cnt -= 1
            elif letter in OPERATORS:
                state = True
            else:
                return False
        if bracket_cnt < 0: return False
    return bracket_cnt == 0 and not state


def includes_good_symbols(exp: str) -> bool:
    res = [letter in ALL_SYMBOLS for letter in exp]
    return all(res)
