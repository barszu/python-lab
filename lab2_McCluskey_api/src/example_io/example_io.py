def input_generator():
    n = 4 #with n = 4 we have 16 possible inputs
    for i in range(2**n):
        yield f'{i:04b}' , i

# print("Input generator:")
# for i in input_generator():
#     print(i)

def output_fun(input_bin, input_int):
    # f(x) = x-1
    if input_int == 0:
        # return f'{0:04b}', 0
        num = 0
        return f'{num:04b}', num
    return f'{input_int-1:04b}', input_int-1
