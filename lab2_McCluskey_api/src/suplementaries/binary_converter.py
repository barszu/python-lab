def to_binary(decimal: int, bites_no: int, full_fill: bool = True) -> str:
    """Converts a decimal number to binary"""
    if decimal.bit_length() > bites_no:
        raise ValueError("Number is too big to be represented with given number of bites")

    binary: str = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary.rjust(bites_no, '0') if full_fill else binary


def from_binary(binary: str) -> int:
    """Converts a binary number to decimal"""
    decimal: int = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * 2 ** (len(binary) - i - 1)
    return decimal


def get_lengthen_binary(binary: str, new_bites_no: int) -> str:
    """Returns a binary number with new length"""
    return binary.rjust(new_bites_no, '0')