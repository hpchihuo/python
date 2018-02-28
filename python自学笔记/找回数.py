# -*- coding: utf-8 -*-
def is_palindrome(n):
    str1 = str(n)
    str2 = str1[::-1]
    if str1 == str2:
        return True
    else:
        return False
