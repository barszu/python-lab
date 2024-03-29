from lab2.global_const import NORMAL_OPERATORS as OPERANDS


def expression_generator(variables: [str], max_len: int) -> str:

    def is_contains_variables(S: str):
        d = {v: 0 for v in variables}
        for c in S:
            if c in d.keys(): d[c] += 1
        return all([cnt >= 1 for _, cnt in d.items()])

    """
        :param l - variable_count:
        :param o - operators_count:
        :param m - negations_count:
        :param S - expression:
        """
    def dfs(l: int, o: int, m: int, S: str): #TODO: na bfs aby znajdowalo najkrotsze najszybciej !!!
        if l + o + m <= max_len:
            if (o == l-1) and is_contains_variables(S):
                # wyrazenie S jest poprawne
                yield S
            if o <= l - 2:
                # mozna dorzucic operator
                for op in OPERANDS:
                    yield from dfs(l, o + 1, m, S + op)
            if l >= 1:
                if S[-1] != '~': #bez sensu jest a~~ bo to a
                    # mozna dorzucic negacje
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

def expression_generator2(variables: [str], max_len: int) -> str:

    def is_contains_variables(S: str):
        d = {v: 0 for v in variables}
        for c in S:
            if c in d.keys(): d[c] += 1
        return all([cnt >= 1 for _, cnt in d.items()])

    def bfs():
        queue = deque([(0, 0, 0, "")])
        while queue:
            l, o, m, S = queue.popleft()
            if l + o + m <= max_len:
                if (o == l - 1) and is_contains_variables(S):
                    yield S
                if o <= l - 2:
                    for op in OPERANDS:
                        queue.append((l, o + 1, m, S + op))
                if l >= 1:
                    if S[-1] != '~':
                        queue.append((l, o, m + 1, S + '~'))
                if not (max_len - len(S) == l - o - 1):
                    for v in variables:
                        queue.append((l + 1, o, m, S + v))

    yield from bfs()

# Przykładowe użycie
# for expression in expression_generator2(['A', 'B'], 5):
#     print(expression)


# test
# print([exp for exp in expression_generator(["a", "b"], 6)])


