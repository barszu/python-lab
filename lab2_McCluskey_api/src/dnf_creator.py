from match_io import match_io
from src.suplementaries.true_table import reduce_table
from src.suplementaries.util import wyr_without_brackets


def create_dnf_for_each_output(input_generator, output_generator, input_variables_repr, output_variables_repr):
    # input_generator - generator of binary strings | int
    # output_generator - generator of binary strings outputs for each input | int

    # input_variables_repr - list of inputted variables names
    # output_variables_repr - list of outputted variables names

    bin_match, int_match = match_io(input_generator, output_generator)
    output_str_len = max([len(x) for x in bin_match.values()])
    input_str_len = max([len(x) for x in bin_match.keys()])
    if input_str_len != len(input_variables_repr):
        raise ValueError("Input binary string length is different than input variables repr length, cannot create DNF!")
    if output_str_len != len(output_variables_repr):
        raise ValueError("Output binary string length is different than output variables repr length, cannot create DNF!")

    # bin_match = {'00': '00', '01': '00', '10': '10', '11': '01'}

    dnf_functions = {} #for each output byte xyz (left to right)
    for pos in range(output_str_len):
        true_inputs = set() #only true inputs on output byte pos
        for input_bin, output_bin in bin_match.items():
            if output_bin[pos] == '1':
                true_inputs.add(input_bin)

        reduced_table = reduce_table(true_inputs)
        dnf_expr = wyr_without_brackets(reduced_table, input_variables_repr)  # bez zbednego nawiasowania

        dnf_functions[output_variables_repr[pos]] = dnf_expr
    return dnf_functions

def create_dnf(bin_match , input_variables_repr, output_variables_repr):
    output_str_len = max([len(x) for x in bin_match.values()])
    input_str_len = max([len(x) for x in bin_match.keys()])
    if input_str_len != len(input_variables_repr):
        raise ValueError("Input binary string length is different than input variables repr length, cannot create DNF!")
    if output_str_len != len(output_variables_repr):
        raise ValueError(
            "Output binary string length is different than output variables repr length, cannot create DNF!")



    dnf_functions = {}  # for each output byte xyz (left to right)
    for pos in range(output_str_len):
        true_inputs = set()  # only true inputs on output byte pos
        for input_bin, output_bin in bin_match.items():
            if output_bin[pos] == '1':
                true_inputs.add(input_bin)

        reduced_table = reduce_table(true_inputs)
        dnf_expr = wyr_without_brackets(reduced_table, input_variables_repr)  # bez zbednego nawiasowania

        dnf_functions[output_variables_repr[pos]] = dnf_expr
    return dnf_functions



