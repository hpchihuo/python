# -*- coding: utf-8 -*-
def trim(s):
    i = 0
    j = len(s) - 1
    #检查字符串是否全为空格
    if s == ' ' * len(s):
        return ''
    
    while s[i] == ' ':
        i = i + 1
    while s[j] == ' ':
        j = j - 1
    return s[i:j+1]