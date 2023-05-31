#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Figure:

    def get_name(self):
        return "This is fugure"

class Restangle(Figure):
    def get_name(self):
        return "This is restangle"

    def length(self, a, b):
        return (a+b)*2

class Square(Restangle):
    def get_name(self):
        return "This is square"

    def length(self, a):
        return super().length(a, a)


#figure = Figure()
#print(figure.get_name(), figure.length()) # такого метода в Figure не существует

restangle = Restangle()
print(restangle.get_name(), restangle.length(10,20))

square = Square()
print(square.get_name(), square.length(10))
