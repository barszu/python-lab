from lab2.util import redukuj as merge_into_table , minp as minimalize_table , wyr as make_expression

def reduce_table(true_set_strings):
    reduced_inputs = merge_into_table(true_set_strings)
    minimalized_inputs = minimalize_table(true_set_strings , reduced_inputs)
    if minimalized_inputs is not None:
        reduced_inputs = minimalized_inputs
    return reduced_inputs

# def make_dnf_reduced_expression(true_set_strings: set(str)) -> str:
#     dnf_expr = make_expression(reduce_table(true_set_strings))
#     return dnf_expr