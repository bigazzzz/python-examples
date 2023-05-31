#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

text = 'Hello, world!'
pattern = r'([\S]+)(,\s)([\S]+)!'

print(re.match(pattern,text))
print(re.match(pattern,text).group())
print(re.match(pattern,text).group(3))
print(re.match(pattern,text).groups())

