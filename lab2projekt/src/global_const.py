import string

#stale i parametry globalne

VAR = string.ascii_lowercase
OPEN_BRACKET = "("
CLOSE_BRACKET = ")"
OPERATORS = {"&", "|", ">", "^", "/", "~"}
SPECIAL_SYMBOLS = {"T", "F" , "0" , "1"}

LITERAL = set(VAR).union(SPECIAL_SYMBOLS)

ALL_SYMBOLS = LITERAL.union(OPERATORS).union({OPEN_BRACKET , CLOSE_BRACKET})


#uzycie tylko w lab2B
NORMAL_OPERATORS = {"&", "|", ">", "^", "/"}


def get_priority(c):
    if c == '!': return 4 #not
    if c == '^': return 3 #xor
    elif c in ['&', '|', '/']: return 2 #and, or, disjunction
    elif c == '>': return 1 #implication
    else: return -1
