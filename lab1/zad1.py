from global_const import OPEN_BRACKET, CLOSE_BRACKET, VAR, OPERATORS


def check_brackets(exp: str):
    stack = 0
    for letter in exp:
        if letter == OPEN_BRACKET:
            stack += 1
        elif letter == CLOSE_BRACKET:
            stack -= 1
        if stack < 0:
            return False
    return stack == 0


def check_state(exp: str):
    state = True
    for letter in exp:
        if letter == OPEN_BRACKET or letter in VAR:
            state = True
        elif letter == CLOSE_BRACKET or letter in OPERATORS:
            state = False


# sprawdza czy wyrażenie jest poprawne składniowo
# nwm czy dziala
def check(exp: str):
    if not check_brackets(exp):
        return False
    if not check_state(exp):
        return False
    return True


def check2(exp: str):
    state = True
    bracket_cnt = 0
    for letter in exp:
        if state:
            if letter == OPEN_BRACKET:
                bracket_cnt += 1
            elif letter in VAR:
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
