#tlumaczenie zbioru asocjacyjnego na zbior stringow
# potrzebne do polaczania z API z labow

# tluamczenie zbioru asocjacyjnego na zbior stringow
def translate_asignments_to_str_set(true_table: [{str:str}]):
    result_dict:set(str) = set() #tylko wartosci typu 'a':1 , 'b':0 -> '10'
    for input_set in true_table:
        res = [(k, v) for k, v in input_set.items()]
        res.sort()
        res = [v for k, v in res]
        res = "".join(res)
        result_dict.add(res)
    return result_dict

# tlumaczenie zbioru stringow na zbior asocjacyjny
def translate_str_set_to_asignments(str_set: {str} , variables: {str}) -> [{str:str}]:
    variables = list(variables)
    variables.sort()
    result = []
    for string_input in str_set:
        input_dict = {variables[idx]:string_input[idx] for idx in range(len(variables)) if string_input[idx] in ['0', '1']}
        result.append(input_dict)
    return result