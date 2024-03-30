# very time consuming!!!!
from expressions_generator import expression_generator_bfs
from expression_util import check_expression_with_table


def brute_force_finder(true_table: [{str:str}], variables:{str}, max_lenght) -> str:
    best_found = None
    best_len = max_lenght+1 #len of best found expression
    for expr in expression_generator_bfs(list(variables) , max_lenght):
        # print(f'....Checking: {expr}')
        if check_expression_with_table(expr, true_table):
            if len(expr) < best_len:
                best_found = expr
                best_len = len(expr)
                break
    return best_found