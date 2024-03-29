# odwrotna notacja polska korzysta ze stosu dodaje zabiera przy operacji
# a+b -> ab+ najpierw arugemnety pozniej dzialanie

# przekladka na notacje korzysta z rekurencji (odrocony dfs)

from global_const import OPEN_BRACKET, CLOSE_BRACKET, VAR, OPERATORS
from zad1 import check2


def bracket(expr: str):
    if len(expr) == 0: return expr
    if expr[0] == OPEN_BRACKET and expr[-1] == CLOSE_BRACKET and check2(expr[1:-1]):
        return bracket(expr[1:-1])
    return expr
