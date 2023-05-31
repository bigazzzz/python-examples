#!/usr/bin/env python
# -*- coding: utf-8 -*-

import example_circle_math_module as circ_math

r = int(input('радиус=>'))

print('Длина окружности = '+ str(circ_math.circuit(r)))
print('Площадь окружности = '+ str(circ_math.circle_area(r)))

