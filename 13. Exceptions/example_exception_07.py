#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback

x = 10
y = input("Введите число => ")

try:
    y = int(y)
    result = x/y
except:
    log_file = open("log.txt", "a+")
    traceback.print_exc(file=log_file)
    log_file.close()
    result = "Результат не получен"

print(result)
