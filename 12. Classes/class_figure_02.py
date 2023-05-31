#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Figure:

    def get_name(self):
        return "This is fugure"

class Restangle(Figure):
    def get_name(self):
        return "This is restangle"

figure = Figure()
print(figure.get_name())

restangle = Restangle()
print(restangle.get_name())
