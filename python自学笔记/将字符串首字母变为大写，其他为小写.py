# -*- coding: utf-8 -*-
from functools import reduce

def normalize(name):
    name = name[0].upper() + name[1:].lower()
    return name


#利用reduce求累积
def prod(L):
    def prod1(x, y):
        return x*y
    return reduce(prod1,L)

