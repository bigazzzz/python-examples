#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = 10
y = input("Введите число => ")

try:
    y = int(y)
    if y>10:
        raise ValueError()
    result = x/y
except ValueError:
    result = "Необходимо ввести число меньшее или равное 10"
except ZeroDivisionError:
    result = "На ноль делить нельзя"
except:
    result = "что-то еще работает не так как надо, потому что мы не смогли разобраться в чем проблема"

print(result)
