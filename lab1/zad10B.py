# sprawdza tozsamosc dwoch wyrazen logicznych
from zad6 import gen
from zad5 import get_variables
from zad2 import bracket #scina zewnetrzne nawiasy
from zad3 import bal #najbardziej prawa pozycja danego operatora

def change_not_to_xor(expr: str) -> str:
    expr = expr.replace("~", "1^")
    return expr

def to_map(expr: str, vec: str):
    i = 0
    for var in sorted(list(get_variables(expr))):
        expr = expr.replace(var, vec[i])
        i += 1
    expr.replace("T", "1")
    expr.replace("F", "0")
    return expr

def value(expr):
    st = []
    for letter in expr:
        if letter in "01":
            st.append(int(letter))
        elif letter == '|':
            st.append(st.pop() or st.pop())
        elif letter == '&':
            st.append(st.pop() and st.pop())
        elif letter == '>':
            st.append(st.pop() or not st.pop())
        elif letter == '^':
            st.append(st.pop() ^ st.pop())
        elif letter == '~':
            st.append(not st.pop())
        else:  # rzuc blad
            raise ValueError("Invalid operator")
    return st.pop()

def reversed_polish_notation(expr: str):
    if len(expr)==0: return ""
    expr = bracket(expr)
    expr = change_not_to_xor(expr)
    # if expr[0] == "~":
    #     return reversed_polish_notation(expr[1]) + "~" + reversed_polish_notation(expr[2:])
    for operator in ["^" , ">", "|&" ]: #od najmniejszego priorytety do najwiekszego
        if operator == "~":
            if p := bal(expr, operator):
                # return reversed_polish_notation(expr[len(expr)-p :]) + expr[p]
                return reversed_polish_notation(expr[p+1:]) + expr[p]
        else:
            if p := bal(expr, operator): #idx ostatniego operatora przy obroceniu
                a = reversed_polish_notation(expr[:p])
                b = reversed_polish_notation(expr[p + 1:])
                return a + b + expr[p]

    return expr



def equivalence(expr1: str, expr2: str) -> bool:
    if get_variables(expr1) != get_variables(expr2):
        raise ValueError("Different variables!")

    all_combinations = gen(len(get_variables(expr1)))
    for vec in all_combinations:
        if value(reversed_polish_notation(to_map(expr1, vec))) != value(reversed_polish_notation(to_map(expr2, vec))):
            return False
    return True



# print(reversed_polish_notation("~a&b"))
# print(reversed_polish_notation("a>b|c"))
print(equivalence("a>b","~a|b"))
print(equivalence("a>b","~a&b"))




