from global_const import *
# TODO: implement the following functions

def to_implication(expr: str) -> str:
    pattern = '~x|y'
    return expr.replace(">", "|~")