from dnf_creator import create_dnf_for_each_output


def input_generator():
    literals = ['x', 'y', 'M', 'nf2', 'nf1', 'nf0'] #do gory
    n = len(literals) #with n = 4 we have 16 possible inputs
    for i in range(2**n):
        binary = bin(i)[2:].zfill(n)
        yield binary , {k:v for k,v in zip(literals, binary)}

def output_fun(input_bin, input_int):
    d = input_int
    if d['M'] == '0':
        if d['x'] == '0' and d['y'] == '0' and d['nf0'] == '0': #0 floor
            return '011' , 1
        if d['x'] == '0' and d['y'] == '1' and d['nf1'] == '0': #1 floor
            return '101' , 1
        if d['x'] == '1' and d['y'] == '0' and d['nf2'] == '0': #2 floor
            return '110' , 1
    return '111' , 0

#
i = input_generator()
o = output_fun
# print('output_fun_minus1')
# print(create_dnf_for_each_output(i, o, 'xyABD', 'o'))


print(create_dnf_for_each_output(i, o, 'xyM210', '012'))

for i in input_generator():
    a , b = output_fun(i[0], i[1])
    # print(' '.join(list(i[0])))
    print(' '.join(list(a)))
#     # print(i[0] + " | " + a)
#     print(a)
#     decimal = int(a, 2)
#     hexi = hex(decimal)[2:].zfill(8)
    # print(decimal)
    # print(hexi)
#     # print(f"{i[0]} | {i[1]} || {a}")

def eval_logical_expression0(variables):
    # Pobieramy wartości dla każdej zmiennej
    M = int(variables['M'])
    y = int(variables['y'])
    x = int(variables['x'])
    O = int(variables['0'])

    # Wykonujemy operację OR na wartościach
    result = M or y or x or O
    return str(int(result))

def eval_logical_expression1(variables):
    # Pobieramy wartości dla każdej zmiennej
    M = int(variables['M'])
    y = int(variables['y'])
    x = int(variables['x'])
    J = int(variables['1'])

    # Wykonujemy operację OR na wartościach
    result = M or (not y) or x or J
    return str(int(result))

def eval_logical_expression2(variables):
    # Pobieramy wartości dla każdej zmiennej
    M = int(variables['M'])
    y = int(variables['y'])
    x = int(variables['x'])
    D = int(variables['2'])

    # Wykonujemy operację OR na wartościach
    result = M or y or (not x) or D
    return str(int(result))

print("###################")
for i in range(2**6):
    binary = bin(i)[2:].zfill(6)
    variables = {k:v for k,v in zip(['x', 'y', 'M', '2', '1', '0'], binary)}
    res = ""
    res += eval_logical_expression0(variables)
    res += eval_logical_expression1(variables)
    res += eval_logical_expression2(variables)
    # print(res)
    decimal = int(res, 2)
    hexi = hex(decimal)[2:].zfill(8)
    # print(hexi)
    print(f"{i} | {int(res,2)} ")






