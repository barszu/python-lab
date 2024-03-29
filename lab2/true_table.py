from infix_to_postfix_eval import infix_to_postfix, value

#aka main of that module
def create_true_set(exp: str) -> set[str]:
    true_set = set()
    all_combinations = gen_all_combinations(len(get_variables(exp)))
    for vec in all_combinations:
        mapped_exp = to_map(exp, vec)

        rpn = infix_to_postfix(mapped_exp)
        val = value(rpn)

        if val == 1:
            true_set.add(vec)
    return true_set


def get_all_vector_combinations(exp: str) -> set[str]:
    all_combinations = gen_all_combinations(len(get_variables(exp)))

def get_variables(expr: str) -> set[str]:
    return set(expr).intersection(set("abcdefghijklmnopqrstuvwxyz"))

def gen_all_combinations(n: int) -> list[str]:
    if n == 0:
        return [""]
    return [first + other_part for first in ["0", "1"] for other_part in gen_all_combinations(n - 1)]


def to_map(expr: str, vec: str):
    i = 0
    for var in sorted(list(get_variables(expr))):
        expr = expr.replace(var, vec[i])
        i += 1
    expr.replace("T", "1")
    expr.replace("F", "0")
    return expr
