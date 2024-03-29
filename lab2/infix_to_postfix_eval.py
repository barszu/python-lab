from lab2.decorators import bracket
from lab2.global_const import LITERAL


def get_priority(c):
    if c == '!': return 4 #not
    if c == '^': return 3 #xor
    elif c in ['&', '|', '/']: return 2 #and, or, disjunction
    elif c == '>': return 1 #implication
    else: return -1

def change_not_form(expr: str) -> str: #zeby not byl 2 argumentowy -> awaluawane to bedzie jako xor, ale z priorytetem not
    expr = expr.replace("~", "1!")
    return expr

def associativity(c):
    if c == '^':
        return 'R'
    return 'L'  # Default to left-associative


def infix_to_postfix(expression): #chb dziala
    expression = change_not_form(expression)
    result = []
    stack = []

    for i in range(len(expression)):
        c = expression[i]

        # If the scanned character is an operand, add it to the output string.
        if c in LITERAL: result.append(c)
        # If the scanned character is an ‘(‘, push it to the stack.
        elif c == '(':
            stack.append(c)
        # If the scanned character is an ‘)’, pop and add to the output string from the stack
        # until an ‘(‘ is encountered.
        elif c == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # Pop '('
        # If an operator is scanned
        else:
            while stack and (get_priority(expression[i]) < get_priority(stack[-1]) or
                             (get_priority(expression[i]) == get_priority(stack[-1]) and associativity(expression[i]) == 'L')):
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


def value(expr): #przerobic na dzialajace
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
            elif letter == '~': #TODO doklejone
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



# # Driver code
# exp = "(~0|0)&(1|0|0)"
# # Function call
# res = infix_to_postfix(exp)
# print(res)
# print(value(res))


# exp = '(a&~b)|(~a&b)'
# exp = '((c&d)&~b)|(~(c&d)&b)'
# res = infix_to_postfix(exp)
# print(res)