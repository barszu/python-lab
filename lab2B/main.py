from lab2.infix_to_postfix_eval import infix_to_postfix, postfix_to_infix
from lab2.util import wyr_without_brackets
from lab2B.evaluator import get_variables, check_expression_with_table
from lab2B.expressions_generator import expression_generator2
from lab2B.reductor import reduce_table
from lab2B.true_table import create_true_inputs_table

def translate_asignments_to_str_set(true_table: [{str:str}]):
    result_dict:set(str) = set() #tylko wartosci typu 'a':1 , 'b':0 -> '10'
    for input_set in true_table:
        res = [(k, v) for k, v in input_set.items()]
        res.sort()
        res = [v for k, v in res]
        res = "".join(res)
        result_dict.add(res)
    return result_dict

#@deprecated
def translate_str_set_to_asignments(str_set: {str} , variables: {str}) -> [{str:str}]:
    variables = list(variables)
    variables.sort()
    result = []
    for string_input in str_set:
        input_dict = {variables[idx]:string_input[idx] for idx in range(len(variables)) if string_input[idx] in ['0', '1']}
        result.append(input_dict)
    return result

# very time consuming!!!!
def brute_force_finder(true_table: [{str:str}], variables:{str}, max_lenght) -> str:
    best_found = None
    best_len = max_lenght+1 #len of best found expression
    for expr in expression_generator2(list(variables) , max_lenght):
        # print(f'....Checking: {expr}')
        if check_expression_with_table(expr, true_table):
            if len(expr) < best_len:
                best_found = expr
                best_len = len(expr)
                break
    return best_found

def main_reduce_expr(expr) -> str:
    #TODO: to wyrazenie moze byc czym kolwiek trzeba je zweryfikowac!
    expr = expr.replace(" ", "")
    expr = expr.replace("F", "0")
    expr = expr.replace("T", "1")
    try:
        rpn_expr = infix_to_postfix(expr)  # moze byc niepoprawne ale jest w odwroconej notacji polskiej
        # print(rpn_expr)
        true_table = create_true_inputs_table(rpn_expr)
        # print(true_table)
    except ValueError:
        #bad input cannot parse
        print(f'CRITICAL: Bad input! : {expr}')
        return None

    variables_set = get_variables(rpn_expr)

    if len(true_table) == 0:
        return 'F' #wyrazenie zawsze falszywe
    if len(true_table) == 2**len(variables_set):
        return 'T' #wyrazenie zawsze prawdziwe (tautologia)

    #stworz postac DNF ze starego API
    translated_table = translate_asignments_to_str_set(true_table)
    reduced_translated_table = reduce_table(translated_table)

    dnf_expr = wyr_without_brackets(reduced_translated_table, variables_set)
    # return dnf_expr
    #teraz brute forca uruchamiamy, najbardziej optymalnym rozwiazaniem jest dnf_expr -> moga zniknać niepotrzebne zmienne
    dnf_variables_set = get_variables(dnf_expr)
    dnf_true_table = create_true_inputs_table(infix_to_postfix(dnf_expr))

    brute_force_found_expr_rpn = brute_force_finder(dnf_true_table, dnf_variables_set, min(len(dnf_expr), len(expr)) - 1)

    bf_expr = postfix_to_infix(brute_force_found_expr_rpn) if brute_force_found_expr_rpn is not None else None

    res = [expr, dnf_expr]
    res += [bf_expr] if bf_expr is not None else []
    res.sort(key=lambda x: len(x))
    return res[0]

if __name__ == '__main__':
    # expr = '(a&b)&c|b&(a&c)'
    # expr = '(a|~a)&b'
    # expr = '(a&~b)|(~a&b) ' #<- to jest najgorsze
    # expr = '~b&~a|c'
    # a = main_reduce_expr(expr)
    # print(a)

    data = ['a>(b&c)', '(a|b)|(c|a|b) ', '~(~a|~b)', '~a|~~b', '(p/q)/(p/q)' , 'a|~a&(b|~b)|F' , '(a&~b)|(~a&b) ']
    data.extend(['(a&b)&c|b&(a&c)', '(a|~a)&b', '(a&~b)|(~a&b)', '~b&~a|c', 'a>(b&c)', '(a|b)|(c|a|b)', '~(~a|~b)', '~a|~~b', '(p/q)/(p/q)', 'a|~a&(b|~b)|F', '(a&~b)|(~a&b)'])
    logic_expressions = [
        'a', 'b', 'c', '~a', '~b', '~c',
        'a&b', '~a&b', 'a&~b', '~a&~b', 'a|b', '~a|b', 'a|~b', '~a|~b',
        'a&~b|c', 'a|~b&c', '(a&b)|(~c&d)', '~(a|b)&(c|d)',
        '~a&~b', '~(a&b)', '~(~a|b)', '~~a&~b',
        'a&(b|c)', '(a&b)|c', 'a|(~b&c)', '~(a&b&c)',
        'a&b|c', '~(a|b)&c', '((a&b)|c)&~(a|(b&c))', 'a&(~b|(c&d))|~(~a&b)|c'
    ]

    data.extend(logic_expressions)
    data.extend(["" , 'a<(b&c)'])
    for d in data: print(d , '-->' ,main_reduce_expr(d))