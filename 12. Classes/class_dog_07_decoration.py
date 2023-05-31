#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Dog: # класс
    def __init__(self, name): # конструктор класса
        self.name = name
        self._legs = 4 # свойство класса - нельзя обращаться напрямую
        print('На свет появился {} c {} ногами'.format(self.name, self.legs))

    @property
    def legs(self):
        return self._legs

    @legs.setter
    def legs(self, legs):
        if 0<=legs<=4:
            self._legs = legs
        else:
            print('*** error - Ног должно быть от 0 до 4')


dog1 = Dog('Шарик')
dog2 = Dog('Барбос')

dog2.legs=3
print('Собаку по кличке {} прооперировали и теперь он c {} ногами'.format(dog2.name, dog2.legs))
dog2.legs=5
print('Собаку по кличке {} прооперировали и теперь он c {} ногами'.format(dog2.name, dog2.legs))

