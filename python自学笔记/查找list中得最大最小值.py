# -*- coding: utf-8 -*-
def findMinAndMax(L):
	#判断是否为空列表
    if not L:
        return (None, None)
    max = L[0]
    min = L[0]    
    for i in L:
        if max < i:
            max = i
    for i in L:
        if min > i:
            min = i    
    return (min, max)