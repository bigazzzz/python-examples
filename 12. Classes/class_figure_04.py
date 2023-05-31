#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Restangle():
    def get_name(self):
        return "This is restangle"

    @staticmethod
    def length(a, b):
        return (a+b)*2

class Square(Restangle):
    def get_name(self):
        return "This is square"

    @staticmethod
    def length(a):
        return Restangle.length(a, a)


print(Restangle.length(10,20))
print(Square.length(10))
