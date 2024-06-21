# very time consuming!!!!
from expressions_generator import expression_generator_bfs
from expression_util import check_expression_with_table

MAX_ITERATIONS = 50000


def brute_force_finder(true_table: [{str:str}], variables:{str}, max_lenght):
    cnt = 0 #cnt do zatrzymania findera jesli za dlugo trwa znajdowanie
    for rpn_expr in expression_generator_bfs(list(variables) , max_lenght):
        # print(f'....Checking: {expr}')
        if check_expression_with_table(rpn_expr, true_table):
            #zwroc pierwszy znalezione wyrazenie ktore jest prawdziwe tylko dla wszystkich inputow
            # jest ono mozliwie najkrotsze w ONP (bo generujemy od najkrotszych)
            # w normalnej notacji moze byc dluzsze (przez nawiasy), ale aby zaoszczedzic moc obliczeniowa zwracam to
            return rpn_expr
        if cnt > MAX_ITERATIONS:
            return None
        cnt += 1
    return None

