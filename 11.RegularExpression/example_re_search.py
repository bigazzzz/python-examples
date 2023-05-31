#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

text = 'Hello, world!'
pattern = r'(?i:h)ello(?#туткомментарий)'
print(re.search(pattern,text).group())
pattern = r'(?i)hello, (world)!'
print(re.search(pattern,text).groups())
print(re.search(pattern,text).group(1))

