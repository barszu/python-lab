import check_expression
import util
from lab2.decorators import bracket
from true_table import create_true_set, get_variables


def main(inputted) -> None:
    # inputted: str = '(a|b)|(c|a|b) ' #input()
    inputted = inputted.replace(" ", "")
    inputted = inputted.replace("F", "0")
    inputted = inputted.replace("T", "1")

    if not (check_expression.check_syntax(inputted) and (check_expression.includes_good_symbols(inputted))):
        print("ERROR")
        return

    variables_no = len(get_variables(inputted))
    true_inputs = create_true_set(inputted)

    if len(true_inputs) == 0:
        print("F")
        return
    if len(true_inputs) == 2**variables_no:
        print("T")
        return

    reducted_true_inputs = util.redukuj(true_inputs)

    #TODO zobacz do tego co to robi bo nie dziala

    # reducted_true_inputs = util.minp(true_inputs, reducted_true_inputs)
    # res_expr = util.wyr(reducted_true_inputs) if reducted_true_inputs is not None else "T"

    res_expr = util.wyr(reducted_true_inputs) #TODO jest kilka problemow ze np literki nie sa po kolei i co z tym zrobic?
    res_expr = bracket(res_expr)
    print(res_expr)

    #sprawdzenie czy res jest == inputted
    # true_inputs_after = create_true_set(res_expr)
    # print(f'true_inputs_after: {true_inputs_after}')

    return


if __name__ == "__main__":
    data = ['a>(b&c)' , '(a|b)|(c|a|b) ' , '~(~a|~b)' , '~a|~~b' , '(p/q)/(p/q)' , '(a&~b)|(~a&b) ' , 'a|~a&(b|~b)|F']
    # TODO: zadanko garka
    # brute forcem generuj wszystkie mozliwe ciagi pod onp i je ewauluj i sprawdz czy sa takie same i jest git
    # jak jest zle napisany w onp to albo stack na koncu ma wiecej niz 1 wartosc albo wysra sie
    # uwazaj z nadawaniem zmiennym wartosci -> zobacz jak to sie dzieje
    # for d in data:
    #     main(d)
    # main('a&b|c')
    # main('b&a|c')
    main('c|b&a')
    main('c|(b&a)')
