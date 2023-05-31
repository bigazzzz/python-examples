#!/usr/bin/env python
# -*- coding: utf-8 -*-
def update_global_a():
    global_a = 10 #+ global_a
    return global_a

global_a =5
print(global_a)
print(update_global_a())
print(global_a)

