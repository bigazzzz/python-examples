#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

text = 'Hello, world!'

pattern = r'(?i:h)ello,'
print(re.sub(pattern,'rock the',text))
pattern = r'(?i)hello, (world)!'
print(re.sub(pattern,r'\1',text))

text = 'Hello. Меня зовут Вася'
pattern = r'([A-z]+).+'
pattern_replace = r'\1.My name is Vasya'
print(re.sub(pattern,pattern_replace,text))

