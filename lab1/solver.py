def value(expr1, expr2, **kwargs):
    # Zdefiniujmy słownik zmiennych logicznych przekazanych jako argumenty
    vars_dict = kwargs

    # Oblicz wartość logiczną dla expr1 i expr2
    value1 = eval(expr1, vars_dict)
    value2 = eval(expr2, vars_dict)

    # Sprawdź czy wartości są równe
    return value1 == value2


# Przykładowe użycie
print(equivalence('a>b', '~a|b', a=True, b=False))  # True
print(equivalence('a>b', '~a&b', a=True, b=False))  # False
