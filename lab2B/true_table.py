from lab2.infix_to_postfix_eval import value
from lab2B.evaluator import get_variables, map_inputs_to_expr
from lab2B.generators import get_variable_all_setting


def create_true_inputs_table(rpn_exp:str) -> [{str:str}]: #throws ValueError
    true_inputs = []
    for input_set in get_variable_all_setting(get_variables(rpn_exp)):
        mapped_expr = map_inputs_to_expr(rpn_exp, input_set) #przypisanie zmiennym w wyrazeniu wartosci
        if value(mapped_expr):
            true_inputs.append(input_set)
    return true_inputs

#TODO: przepisac garkowe funkcje zeby dzialaly ze slownikami -> albo ogarnac ich dzialanie i zostac na starym API
def reduce(true_table):  # reduduje zbior co daje true wartosci
    reduced_true_table = set([])
    b1 = False
    for input_A in true_table:
        b2 = False
        for input_B in true_table:
            n = lacz(input_A, input_B)
            if n:
                reduced_true_table.add(n)
                b1 = b2 = True
        if not b2:
            reduced_true_table.add(input_A)
    if b1:
        return redukuj(reduced_true_table)
    else:
        return reduced_true_table
