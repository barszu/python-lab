# sprawdza tozsamosc dwoch wyrazen logicznych
from zad7 import value
from zad4 import reversed_polish_notation , reversed_polish_notation2
from zad6 import gen
from zad5 import get_variables, to_map2 as to_map


def equivalence(expr1: str, expr2: str) -> bool:
    if get_variables(expr1) != get_variables(expr2):
        raise ValueError("Different variables!")

    all_combinations = gen(len(get_variables(expr1)))
    for vec in all_combinations:
        if value(reversed_polish_notation(to_map(expr1, vec))) != value(reversed_polish_notation(to_map(expr2, vec))):
            return False
    return True

#nie dziala z ~
print(reversed_polish_notation2("~a&b"))
print(reversed_polish_notation2("a>b"))
# print(equivalence("a>b","~a|b"))
# print(equivalence("a>b","~a&b"))

