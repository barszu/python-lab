def get_sequence(lenth:int, letters: list[str]): #o dlugosci lenth z liter letters
    if lenth==0:
        yield ""
    else:
        for seq in get_sequence(lenth - 1 , letters):
            for l in letters:
                yield seq+l

# test
# for i in get_sequence(4, ['0' , '1']):
#     print(i)

def get_variable_all_setting(variables:[str]): #zbuduj slownik mapujacy zmienne
    for seq in get_sequence(len(variables) , ['0' , '1']):
        yield {v:seq[idx] for idx , v in enumerate(variables)}

# test
# for i in get_variable_setting(['a' , 'b']):
#     print(i)

