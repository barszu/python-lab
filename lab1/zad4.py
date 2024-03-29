from zad2 import bracket
from zad3 import bal


def reversed_polish_notation(expr: str):
    expr = bracket(expr)
    for operator in [">", "|&", "^", "~"]: #od najmniejszego priorytety do najwiekszego
        if p := bal(expr, operator):
            return reversed_polish_notation(expr[:p]) + reversed_polish_notation(expr[p + 1:]) + expr[p]
    return expr


def reversed_polish_notation2(expr: str):
    if len(expr)==0: return ""
    expr = bracket(expr)
    if expr[0] == "~":
        return reversed_polish_notation2(expr[1]) + "~" + reversed_polish_notation2(expr[2:])
    for operator in [">", "|&", "^"]: #od najmniejszego priorytety do najwiekszego
        if p := bal(expr, operator):
            return reversed_polish_notation2(expr[:p]) + reversed_polish_notation2(expr[p + 1:]) + expr[p]
    return expr