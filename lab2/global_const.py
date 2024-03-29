import string

VAR = string.ascii_lowercase
OPEN_BRACKET = "("
CLOSE_BRACKET = ")"
OPERATORS = {"&", "|", ">", "^", "/", "~"}
SPECIAL_SYMBOLS = {"T", "F" , "0" , "1"}

LITERAL = set(VAR).union(SPECIAL_SYMBOLS)

ALL_SYMBOLS = LITERAL.union(OPERATORS).union({OPEN_BRACKET , CLOSE_BRACKET})


#uzycie tylko w lab2B
NORMAL_OPERATORS = {"&", "|", ">", "^", "/"}

