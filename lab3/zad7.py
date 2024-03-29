def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def primes():
    n = 2
    while True:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                break
        else:
            yield n
        n += 1

def gemini_numbers():
    # liczby pierwsze co roznia sie o 2
    generator = primes()
    old = next(generator)
    new = next(generator)
    while True:
        if new - old == 2:
            yield (old, new)
        old, new = new, next(generator)



#test
# for i in fib():
#     print(i)
#     if i> 100: break
#
# for i in primes():
#     print(i)
#     if i > 100: break
#
# gen = primes()
# print(next(gen))
# print(next(gen))

# g = gemini_numbers()
# print(next(g))
# print(next(g))
# print(next(g))

def gen(n):
    if n==0:
        yield ""
    else:
        for c in gen(n-1):
            yield c+'0'
            yield c+'1'

g = gen(3)
print(next(g))
print(next(g))
print(next(g))

def permutations(string):
    if len(string) == 1:
        yield string
    else:
        for i in range(len(string)):
            for p in permutations(string[:i] + string[i+1:]):
                yield string[i] + p

g = permutations("abc")
print(next(g))
print(next(g))
print(next(g))

def kombinations(string , k):
    if k == 1:
        for c in string:
            yield c
    elif len(string) == k: yield string
    else:
        for comb in kombinations(string[1:], k-1):
            yield string[0] + comb
        for comb in kombinations(string[1:], k):
            yield comb

g = kombinations("abc", 2)
print([i for i in g])

def wariacje_bez_powtorzen(string, k):
    for comb in kombinations(string, k):
        # for perm in permutations(comb):
        #     yield perm
        yield from permutations(comb)

g = wariacje_bez_powtorzen("abc", 2)
print([i for i in g])

def podzbiory(string):
    if len(string) == 0:
        yield ""
    else:
        for sub in podzbiory(string[1:]):
            yield sub
            yield string[0] + sub

g = podzbiory("abc")
print([i for i in g])

def zadanie():
    cyfry = [i for i in range(1,10)]
    liczby = [i for i in podzbiory(cyfry)]





