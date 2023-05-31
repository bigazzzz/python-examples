#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = 10
y = input("Введите число => ")

try:
    y = int(y)
    result = x/y
except:
    result = "Что-то пошло не так"

print(result)
