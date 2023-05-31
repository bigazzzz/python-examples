#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

text = "Hello. Меня зовут Вася и мне 15 лет"

pattern = r'\d+'
print(re.findall(pattern, text))
pattern = r'^\D'
print(re.findall(pattern, text))
pattern = r'[\d\D]+'
print(re.findall(pattern, text))
pattern = r'[\s\S]+'
print(re.findall(pattern, text))
pattern = r'зовут\s([А-я]+)\s'
print(re.findall(pattern, text))

