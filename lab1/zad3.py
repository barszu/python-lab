from global_const import OPEN_BRACKET, CLOSE_BRACKET, VAR, OPERATORS

#najbardziej prawa pozycja danego operatora

def bal(expr: str, operators):
    bracket_cnt = 0
    for i, letter in enumerate(expr[::-1]):
        if letter == CLOSE_BRACKET:
            bracket_cnt += 1
        elif letter == OPEN_BRACKET:
            bracket_cnt -= 1
        elif letter in operators and bracket_cnt == 0:
            return i
    return None
