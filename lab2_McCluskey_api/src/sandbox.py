def first(args):
    x = int(args['x'])
    y = int(args['y'])
    one = int(args['1'])

#comprarator
def input_generator():
    literals = ['x', 'y', '1', '2down', '2up', '3']
    n = len(literals)
    for i in range(2**n):
        binary = bin(i)[2:].zfill(n)
        yield binary, {k:v for k,v in zip(literals, binary)}

def output_fun(input_bin, input_int): #1 2down 2up 3
    d = input_int
    res = {'1': '0', '2down': '0', '2up': '0', '3': '0'}
    if d['x'] == '0' and d['y'] == '0' and d['1'] == '1': #1 floor
        res['1'] = '1'
    if d['x'] == '0' and d['y'] == '1' and d['2down'] == '1': #2 floor down
        res['2down'] = '1'
    if d['x'] == '0' and d['y'] == '1' and d['2up'] == '1': #2 floor up
        res['2up'] = '1'
    if d['x'] == '1' and d['y'] == '0' and d['3'] == '1': #3 floor
        res['3'] = '1'
    return f"{res['1']}{res['2down']}{res['2up']}{res['3']}", res

print('x y 1 2down 2up 3 | 1 2down 2up 3')
for i in input_generator():
    a , b = output_fun(i[0], i[1])
    # print(f"{i[0]} | {a}")
    # print(a)
    print(i[0])

#delayer

def input_generator():
    literals = ['1', '2', '3', '4', 'C']
    n = len(literals)
    for i in range(2**n):
        binary = bin(i)[2:].zfill(n)
        yield binary, {k:v for k,v in zip(literals, binary)}

def output_fun(input_bin, input_int): #1 2down 2up 3
    d = input_int
    res = {'1': '0', '2': '0', '3': '0', '4': '0'}
    if d['C'] == '1':
        if d['1'] == '1':
            res['1'] = '1'
        if d['2'] == '1':
            res['2'] = '1'
        if d['3'] == '1':
            res['3'] = '1'
        if d['4'] == '1':
            res['4'] = '1'
    return f"{res['1']}{res['2']}{res['3']}{res['4']}", res

print('1 2 3 4 C | 1 2 3 4')
for i in input_generator():
    a , res = output_fun(i[0], i[1])
    # print(f"{i[0]} | {a}")
    # print(a)
    # print(' '.join(list(i[0])))
    print(f"{res['1']} {res['2']} {res['3']} {res['4']}")