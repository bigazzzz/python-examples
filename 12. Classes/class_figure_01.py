#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Figure:

    def get_name(self):
        return "This is fugure"

class Restangle(Figure):
    pass # не делаем ничего

figure = Figure()
print(figure.get_name())

restangle = Restangle()
print(restangle.get_name())
