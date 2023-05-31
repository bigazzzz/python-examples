#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

text = "Hello. Меня зовут Вася и мне 15 лет"

pattern = r'.+'
print(re.findall(pattern, text)) # ['Hello. Меня зовут Вася и мне 15 лет']
pattern = r'^.'
print(re.findall(pattern, text)) # ['H']
pattern = r'[0-9]+'
print(re.findall(pattern, text)) # ['15']
pattern = r'[A-z]{1,2}'
print(re.findall(pattern, text)) # ['He', 'll', 'o']
pattern = r'[А-я]{1,2} [0-9]'
print(re.findall(pattern, text)) # ['не 1']
pattern = r'зовут [А-я]+ '
print(re.findall(pattern, text)) # ['зовут Вася ']
pattern = r'зовут ([А-я]+) '
print(re.findall(pattern, text)) # ['Вася']

pattern = r'^.{4}'
pattern = r'.+ (.+)$'
pattern = r'[^А-я0-9 .]+'





