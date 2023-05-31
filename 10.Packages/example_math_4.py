#!/usr/bin/env python
# -*- coding: utf-8 -*-

import figures
print("*"*60)
print(dir(figures))
print(figures.__doc__)
print(figures.__file__)
print(figures.__name__)
print(figures.__package__)
print(figures.__path__)

import figures.square as square
print("*"*60)
print(dir(square))
print(square.__doc__)
print(square.__file__)
print(square.__name__)
print(square.__package__)

from figures.square import len as square_len
print("*"*60)
print(dir(square_len))
print(square_len.__doc__)
print(square_len.__class__)

print("*"*60)

