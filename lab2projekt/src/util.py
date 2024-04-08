from itertools import *

from decorators import bracket

#API z labow

def lacz(s1, s2):  # laczy 2 wektory tak jak karnough
    lr = 0
    w = ""
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            w += s1[i]
        else:
            w += '-'
            lr += 1
    if lr == 1: return w
    return None


# print(lacz('1010', '1110'))
# print(lacz('1010', '1111'))


def redukuj(s):  # reduduje zbior co daje true
    s2 = set([])
    b1 = False
    for e1 in s:
        b2 = False
        for e2 in s:
            n = lacz(e1, e2)
            if n:
                s2.add(n)
                b1 = b2 = True
        if not b2:
            s2.add(e1)
    if b1:
        return redukuj(s2)
    else:
        return s2


# s = {'0100', '0111', '1001', '1010', '1100', '1101', '1110', '1111'}
# print(s)
# s2 = redukuj(s)
# print(s2)


def wyr(s):  # buduje DNF ze zbioru wektorow
    res = ""
    for e in s:
        res2 = ""
        for i in range(len(e)):
            if e[i] == '-': continue
            if e[i] == '0': res2 += "~"
            res2 += "abcdefg"[i] + '&'
        else:
            res += "(" + res2[:-1] + ")|"
    return res[:-1]

import re
def wyr_without_brackets(s , variables):  #buduje DNF ze zbioru wektorow, stara sie nie wstawiac zbednych nawiasow
    variables = sorted(list(variables))
    res = ""
    for e in s:
        res2 = ""
        for i in range(len(e)):
            if e[i] == '-': continue
            if e[i] == '0': res2 += "~"
            res2 += variables[i] + '&'
        if len(res2[:-1]) == 1:  # jeden znak
            res += bracket(res2[:-1]) + "|"
        elif re.match(r"~[a-z]$", res2[:-1]):  # negacja i zwykla zmienna
            res += bracket(res2[:-1] + "|")
        else:
            res += "(" + res2[:-1] + ")|"
    return bracket(res[:-1])

# print(wyr(s))
# print(wyr(s2))


def match(x, w):  # czy x pasuje do wzorca w
    for i in range(len(x)):
        if w[i] == '-': continue
        if w[i] != x[i]: return False
    return True


# print(match('1010','10--'))
# print(match('1110','-10-'))

def minp(d, w): #d tablica prawdy, w to zmergowane wektory
    # minimalizuje zbior d wektorow tak zeby pasowaly do skroconego zbioru w
    for r in range(1, len(w)):
        for c in combinations(w, r):
            nowy = set()
            for el in d:
                for wz in c:
                    if match(el, wz): nowy.add(el)
            if len(nowy) == len(d): return c

# s3 = minp(s,s2)
# print(s3)
# print(wyr(s3))
