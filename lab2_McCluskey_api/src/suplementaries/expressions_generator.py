from global_const import NORMAL_OPERATORS as OPERANDS
# generatory poprawnych wyrazen logicznych (o dlugosci max_len)
# w postaci ONP dla zmiennych podanych w liscie variables

#zmienne sa niezbedne, zbedne zostaly nie podane

def expression_generator_dfs(variables: [str], max_len: int) -> str:

    def is_contains_variables(S: str): #poprawne wyrazenie musi zawierac wszystkie zmienne
        d = {v: 0 for v in variables}
        for c in S:
            if c in d.keys(): d[c] += 1
        return all([cnt >= 1 for _, cnt in d.items()])

    """
        :param l - variable_count: #ilosc uzytych zmiennych ktore trzeba zaspokoic operatorami
        :param o - operators_count: #ilosc uzytych operatorow
        :param m - negations_count: #ilosc uzytych negacji
        :param S - expression: #poprawne wyrazenie logiczne w postaci ONP (rpn)
    """
    def dfs(l: int, o: int, m: int, S: str): #bfs aby znajdowalo najkrotsze najszybciej
        if l + o + m <= max_len: #poprawne kiedy zachowuje dlugosc
            if (o == l-1) and is_contains_variables(S):
                # wyrazenie S jest poprawne
                yield S
            if o <= l - 2:
                # mozna dorzucic operator
                for op in OPERANDS:
                    yield from dfs(l, o + 1, m, S + op)
            if l >= 1:# mozna dorzucic negacje
                if S[-1] != '~': #bez sensu jest a~~ bo to a
                    yield from dfs(l, o, m + 1, S + '~')
            if not (max_len - len(S) == l-o-1):
                # zawsze mozna dorzucic literke?
                # no chyba zeby wyrazenie bylo poprawne to uzupelnic operatorami
                for v in variables:
                    yield from dfs(l + 1, o, m, S + v)

    gen_helper = dfs(0, 0, 0, "")
    try:
        while True:
            yield next(gen_helper)
    except StopIteration:
        return


from collections import deque

def expression_generator_bfs(variables: [str], max_len: int) -> str:

    def is_contains_variables(S: str):
        d = {v: 0 for v in variables}
        for c in S:
            if c in d.keys(): d[c] += 1
        return all([cnt >= 1 for _, cnt in d.items()])

    """
        :param l - variable_count: #ilosc uzytych zmiennych ktore trzeba zaspokoic operatorami
        :param o - operators_count: #ilosc uzytych operatorow
        :param m - negations_count: #ilosc uzytych negacji
        :param S - expression: #prawie poprawne wyrazenie logiczne w postaci ONP (rpn)
    """
    def bfs():
        queue = deque([(0, 0, 0, "")])
        while queue:
            l, o, m, S = queue.popleft()
            if l + o + m <= max_len: #dlugosc wyrazenia mniejsza
                if (o == l - 1) and is_contains_variables(S): #wyrazenie jest poprawne mozna zwrocic
                    yield S
                if o <= l - 2: #mozna dorzucic operator
                    for op in OPERANDS:
                        queue.append((l, o + 1, m, S + op))
                if l >= 1: #mozna dorzucic negacje
                    if S[-1] != '~': #bez sensu jest a~~ (~~a) bo to a
                        queue.append((l, o, m + 1, S + '~'))
                if not (max_len - len(S) == l - o - 1): #zawsze mozna dorzucic literke,
                    # chyba ze ich jest tak duzo ze trzeba juz wszystkie zaspokajac
                    for v in variables:
                        queue.append((l + 1, o, m, S + v))

    yield from bfs()

# Przykładowe użycie
# for expression in expression_generator_bfs(['A', 'B'], 5):
#     print(expression)



