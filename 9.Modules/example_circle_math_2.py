#!/usr/bin/env python
# -*- coding: utf-8 -*-

from example_circle_math_module import circuit,circle_area

r = int(input('радиус=>'))

print('Длина окружности = '+ str(circuit(r)))
print('Площадь окружности = '+ str(circle_area(r)))


