# demonstracja dzialania podstawowych bramek logicznych

from TTL import *

#tak uzytkownik podaje uklad cyfrowy

inp('a','b') #inputy do ukladu

AND('a','b','and')
NAND('1','b','nand')
OR('a','b','or')
NOR('a','b','nor')
XOR('a','b','xor')
XNOR('a','b','xnor')

out('a','b','and','nand','or','nor','xor','xnor') #outputy z ukladu

build()

