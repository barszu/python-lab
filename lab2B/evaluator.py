from generators import get_variable_all_setting
from lab2.global_const import VAR
from lab2.infix_to_postfix_eval import value


def map_inputs_to_expr(exp:str, input: {str:str}): #mapuje do expr input zmiennych wpisuje pod a np 0
    for variable , set_val in input.items():
        exp = exp.replace(variable, set_val)
    return exp

def get_variables(expr:str) -> [str]:
    return sorted(list(set(expr).intersection(set(VAR))))

def check_expression_with_table(rpn_exp: str, true_inputs: [{str:str}]) -> bool:
    is_good = True
    for input_set in get_variable_all_setting(get_variables(rpn_exp)):
        mapped_expr = map_inputs_to_expr(rpn_exp, input_set) #przypisanie zmiennym w wyrazeniu wartosci
        try:
            val = value(mapped_expr)
            if val:
                if not (input_set in true_inputs):
                    is_good = False
                    break
                #else ok
            else: #== False
                if input_set in true_inputs:
                    #input nie daje prawdy a powinien
                    is_good = False
                    break
                #else ok

        except ValueError:
            print(f'WARNING: bad expression: {rpn_exp}')
            is_good = False
            break

    return is_good

#test
# v = check_expression_with_table('abc&' , [{'a':'1' , 'b':'1'}])
# print(v)