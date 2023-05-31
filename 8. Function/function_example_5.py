#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sum(a,b):
    return a+b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

def minus(a,b):
    return a-b

def summa(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print('Сумма 5 и 4 будет равна = ' + str(sum(5,4)))
print(summa(5,3,4,5,6))
