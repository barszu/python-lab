from global_const import *
from zad2 import bracket



# zamiena odwrocona notacje polska na zwykla

def alg(expr: str) -> str:
    stack = []
    for letter in expr:
        if letter in VAR:
            stack.append(letter)
        elif letter in OPERATORS:
            a = stack.pop()
            b = stack.pop()
            stack.append(f"({b}{letter}{a})")
    return bracket(stack[0])

print(alg("ab&"))
print(alg("ab>c>"))
print(alg("abc|>"))
