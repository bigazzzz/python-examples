#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

text = 'Hello, world!'

pattern = r','
print(re.split(pattern,text))
pattern = r'o'
print(re.split(pattern,text))
pattern = r'\s'
print(re.split(pattern,text))
