from src.example_io.example_io import input_generator, output_fun


def match_io(inputs, output_func):
    # input_generator - generator of binary strings | int
    # output_generator - generator of binary strings outputs for each input | int
    # returns: [{str:str}] - list of dictionaries with input-output pairs

    # input_generator - collection of binary strings | int
    # output_generator - function that conwerst input to output binary | int
    # returns: {str:str} , {int:int} - list of dictionaries with input-output pairs binary | int
    res_bin = {}
    res_int = {}
    for input_bin, input_int in inputs:
        output_bin, output_int = output_func(input_bin , input_int)
        res_bin[input_bin] = output_bin
        # res_int[input_int] = output_int
    return res_bin, res_int


#test
# i = input_generator()
# o = output_fun
# print(match_io(i, o))




