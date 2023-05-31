#!/usr/bin/env python
# -*- coding: utf-8 -*-

def many(*args, **kwargs):
    print( args )
    print( kwargs )

many(1, 2, 3, name="Mike", job="programmer")
