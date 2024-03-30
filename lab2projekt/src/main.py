
from true_table import create_true_inputs_table, reduce_table
from translators import translate_asignments_to_str_set
from brute_force_finder import brute_force_finder
from infix_postfix import infix_to_postfix, postfix_to_infix
from util import wyr_without_brackets
from expression_util import get_variables



def main_reduce_expr(expr) -> str:
    expr = expr.replace(" ", "") #pozbycie sie spacji

    #zamiana wdl konwencji
    expr = expr.replace("F", "0")
    expr = expr.replace("T", "1")
    try:
        rpn_expr = infix_to_postfix(expr)  # moze byc niepoprawne ale jest w odwroconej notacji polskiej
        true_table = create_true_inputs_table(rpn_expr)
    except ValueError:
        #nie poprawne dane wejsciowe, infix_to_postfix rzucil wyjatek albo create_true_inputs_table
        # print(f'CRITICAL: Bad input! : {expr}')
        return "ERROR"

    #zmienne w wyrazeniu
    variables_set = get_variables(rpn_expr)

    if len(true_table) == 0: return 'F' #wyrazenie zawsze falszywe
    if len(true_table) == 2**len(variables_set): return 'T' #wyrazenie zawsze prawdziwe (tautologia)

    #stworz postac DNF z API z zajec
    translated_table = translate_asignments_to_str_set(true_table)
    reduced_translated_table = reduce_table(translated_table)

    dnf_expr = wyr_without_brackets(reduced_translated_table, variables_set) #bez zbednego nawiasowania

    #teraz brute forca uruchamiamy, najbardziej optymalnym rozwiazaniem jest dnf_expr na ten moment
    # -> moga zniknać niepotrzebne zmienne i sie uproscic
    dnf_variables_set = get_variables(dnf_expr)
    dnf_true_table = create_true_inputs_table(infix_to_postfix(dnf_expr))

    brute_force_found_expr_rpn = brute_force_finder(dnf_true_table, dnf_variables_set, min(len(dnf_expr), len(expr)) - 1)

    bf_expr = postfix_to_infix(brute_force_found_expr_rpn) if brute_force_found_expr_rpn is not None else None

    #zwrocenie najkrotszego wyrazenia z 3
    res = [expr, dnf_expr]
    res += [bf_expr] if bf_expr is not None else []
    res.sort(key=lambda x: len(x))
    return res[0]





if __name__ == '__main__':
    inputted = input()
    res = main_reduce_expr(inputted)
    print(res)

