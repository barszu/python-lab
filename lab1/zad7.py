# oblicza wartosc wyrazenia zapisanego z notacji polskiej
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
        else:  # rzuc blad
            pass
    return st.pop()

# tautologia to brute force wszytskich mozliwych obcji dla zmiennych

# TODO zrob tautologie do konca
