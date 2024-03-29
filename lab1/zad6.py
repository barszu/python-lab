# funckja generująca wszytskie 0-1 mozliwe ciagi o dlugosci n

def gen(n: int) -> list[str]:
    if n == 0:
        return [""]
    return [first + other_part for first in ["0", "1"] for other_part in gen(n - 1) ]

# print(gen(3))
# print(gen(4))