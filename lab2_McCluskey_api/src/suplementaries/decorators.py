from src.suplementaries.global_const import OPEN_BRACKET, CLOSE_BRACKET
from src.suplementaries.check_expression import check_syntax

#usuwa zbedne nawiasy (lab)
def bracket(expr: str):
    if len(expr) == 0: return expr
    if expr[0] == OPEN_BRACKET and expr[-1] == CLOSE_BRACKET and check_syntax(expr[1:-1]):
        return bracket(expr[1:-1])
    return expr