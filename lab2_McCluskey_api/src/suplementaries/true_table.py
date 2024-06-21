from src.suplementaries.infix_postfix import value
from src.suplementaries.expression_util import get_variables, map_inputs_to_expr, get_variable_all_setting
from src.suplementaries.util import redukuj as merge_into_table, minp as minimalize_table

#zwraca liste slownikow z wartosciami zmiennych dla ktorych wyrazenie jest prawdziwe
# wyrazenie w postaci ONP (rpn_exp)
def create_true_inputs_table(rpn_exp:str) -> [{str:str}]: #throws ValueError
    true_inputs = []
    for input_set in get_variable_all_setting(get_variables(rpn_exp)):
        mapped_expr = map_inputs_to_expr(rpn_exp, input_set) #przypisanie zmiennym w wyrazeniu wartosci
        if value(mapped_expr):
            true_inputs.append(input_set)
    return true_inputs

# redukuje wejscia w postaci stringow do minimalnej postaci, z uzyciem API z labow
def reduce_table(true_set_strings):
    reduced_inputs = merge_into_table(true_set_strings)
    minimalized_inputs = minimalize_table(true_set_strings , reduced_inputs)
    if minimalized_inputs is not None:
        reduced_inputs = minimalized_inputs
    return reduced_inputs
