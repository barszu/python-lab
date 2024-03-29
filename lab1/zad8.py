from zad4 import reversed_polish_notation
from zad5 import to_map2 as to_map, get_variables
from zad6 import gen
from zad7 import value


def tautology(expr: str) -> bool:
    # ile zmiennych ma expr i zmapowac je z odpowiednimi ciagami
    variables_no = len(get_variables(expr))
    for vec in gen(variables_no):
        # bruteforsowa ewaluacja
        if not value(reversed_polish_notation(to_map(expr, vec))):
            return False
    return True
