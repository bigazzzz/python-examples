#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Dog: # класс
    def __init__(self): # конструктор класса
        self.legs = 4
        self.head = 1
        self.body = 1
        self.tail = True
        print('Собака создалась')

dog1 = Dog() # объект или объект класса Dog
print('Ног - ', dog1.legs)
dog1.legs = 3
print('Ног стало - ', dog1.legs)
dog2 = Dog() # объект или объект класса Dog
print('Ног - ', dog2.legs)
dog2.tail = not dog2.tail
print('Есть хвост? - ', dog2.tail)
