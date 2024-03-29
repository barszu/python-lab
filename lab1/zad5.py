# vec = [1,0,1] mapped into [a,b,c] and gives a=1 , b=0 , c=1

def to_map(expr: str, vec: str):
    # TODO to nie ma sensu
    t = {sorted(list(set(expr).intersection(set(vec))))[i]
         # wypluwa same literki posortowane
         : vec[i] for i in range(len(vec))}  # tworzy slownik t[a] = '1'
    for k in t:
        expr = expr.replace(k, t[k])
    return expr


def get_variables(expr: str) -> set[str]:
    return set(expr).intersection(set("abcdefghijklmnopqrstuvwxyz"))


# vec = [1,0,1] mapped into [a,b,c] and gives a=1 , b=0 , c=1
def to_map2(expr: str, vec: str):
    i = 0
    for var in sorted(list(get_variables(expr))):
        expr = expr.replace(var, vec[i])
        i += 1
    return expr
