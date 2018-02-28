# -*- coding: utf-8 -*-
from functools import reduce

def str2float(s):
    s1,s2 = s.split('.')
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def strToNum(s):
        return DIGITS[s]
    def listToInt(x, y):
        return x*10 + y
    return reduce(listToInt,map(strToNum,s1)) + reduce(listToInt,map(strToNum,s2))/pow(10,len(s2))

s = "1234.8789"
print(str2float(s))