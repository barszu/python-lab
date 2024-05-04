from TTL import *

#tak uzytkownik podaje uklad cyfrowy

inp('a','b') #inputy do ukladu

NAND('a','b','p1')
NAND('a','p1','p2')
NAND('b','p1','p3')
NAND('p2','p3','c')
NAND('a','b','c')

out('a','b','c') #outputy z ukladu

build()