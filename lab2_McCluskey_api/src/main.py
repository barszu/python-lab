#test
from src.dnf_creator import create_dnf_for_each_output, create_dnf
from src.example_io.example_io2 import input_generator, output_fun_div , output_fun_mod, output_fun_minus1

i = input_generator()
o = output_fun_div
print('output_fun_div //10')
print(create_dnf_for_each_output(i, o, 'dcba', 'wzyx'))

i = input_generator()
o = output_fun_mod
print('output_fun_div %10')
print(create_dnf_for_each_output(i, o, 'dcba', 'wzyx'))

# print('custom test')
# print(create_dnf({'00': '00', '01': '00', '10': '10', '11': '01'} , 'ba', 'xy'))

i = input_generator()
o = output_fun_minus1
print('output_fun_minus1')
print(create_dnf_for_each_output(i, o, 'dcba', 'wzyx'))

########################################
def input_generator():
    n = 4 #with n = 4 we have 16 possible inputs
    for i in range(2**n):
        yield f'{i:04b}' , i

def output_fun_minus1(input_bin, input_int):
    # f(x) = x-1 | x = 0 -> 0
    if input_int == 0:
        # return f'{0:04b}', 0
        num = 0
        return f'{num:04b}', num
    return f'{input_int-1:04b}', input_int-1

i = input_generator()
o = output_fun_minus1
print('output_fun_minus1')
print(create_dnf_for_each_output(i, o, 'dcba', 'wzyx'))


i = input_generator()
o = output_fun_minus1
from match_io import match_io
a, b = match_io(i, o)
print("dcba | wzyx")
for k,v in a.items():
    print(k+" | "+v)



