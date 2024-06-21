from decorators import bracket
from global_const import LITERAL, get_priority

def change_not_form(expr: str) -> str:
    #zeby not byl 2 argumentowy -> awaluawane to bedzie jako xor, ale z priorytetem not
    # inaczej infix_to_postfix nie dziala
    expr = expr.replace("~", "1!")
    return expr

def infix_to_postfix(expression): #dziala z not, kiedy zamieniam na XOR
    expression = change_not_form(expression)
    result = []
    stack = []

    for i in range(len(expression)):
        c = expression[i]
        if c in LITERAL:
            result.append(c)

        elif c == '(': stack.append(c)

        elif c == ')': #bierz ze stosu wszystko dopoki nie napotkasz (
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # Pop '('

        #jesli operator to sprawdz czy ma wiekszy priorytet niz na stosie
        else:
            while stack and (get_priority(expression[i]) <= get_priority(stack[-1])):
                result.append(stack.pop())
            stack.append(c)

    # Pop all the remaining elements from the stack
    while stack:
        result.append(stack.pop())

    res = ''.join(result)
    return res


from collections import deque
def postfix_to_infix(exp):
    s = deque()
    for l in exp:
        if l in LITERAL:
            s.appendleft(l)
        elif l == '~':
            op1 = s.pop()
            s.appendleft(bracket("(" + l + op1 + ")"))
        else:
            op1 = s.pop()
            op2 = s.pop()
            s.appendleft("(" + op2 + l + op1 + ")")
    return bracket(s[0])


# print(postfix_to_infix("ab&"))
# print(postfix_to_infix("ab&c|"))
# print(postfix_to_infix("ab~&c|d&"))


def value(expr): #oblicza wartosc wyrazenia w onp
    st = []
    try:
        for letter in expr:
            if letter in "01":
                st.append(int(letter))
            elif letter == '|':
                b = st.pop()
                a = st.pop()
                st.append(a or b)
            elif letter == '&':
                b = st.pop()
                a = st.pop()
                st.append(a and b)
            elif letter == '>':
                b = st.pop()
                a = st.pop()
                st.append(not a or b)
            elif letter == '^' or letter == '!':
                b = st.pop()
                a = st.pop()
                st.append(a ^ b)
            elif letter == '/':
                b = st.pop()
                a = st.pop()
                st.append(not (a and b) )
            elif letter == '~':
                a = st.pop()
                st.append(not a)
            else:  # rzuc blad
                raise ValueError("Invalid operator")
        if len(st) != 1:
            raise ValueError("Invalid expression")
        return st.pop()

    except:
        raise ValueError("Invalid expression")
    return
