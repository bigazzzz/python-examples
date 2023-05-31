#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Dog: # класс
    def __init__(self, name): # конструктор класса
        self.name = name
        self._legs = 4 # свойство класса - нельзя обращаться напрямую
        print('На свет появился {} c {} ногами'.format(self.name, self.legs))

    def set_legs(self, legs):
        if 0<=legs<=4:
            self._legs = legs
        else:
            print('Ног должно быть от 0 до 4')
            
    def get_legs(self):
        return self._legs

    legs = property(get_legs, set_legs)

dog1 = Dog('Шарик')
dog2 = Dog('Барбос')
dog2.set_legs(3)
print('Собаку по кличке {} прооперировали и теперь он c {} ногами'.format(dog2.name, dog2.get_legs()))

dog2.legs=5
print('Собаку по кличке {} прооперировали и теперь он c {} ногами'.format(dog2.name, dog2.get_legs()))

dog2._legs=5 # не делайте так никогда
print('Собаку по кличке {} прооперировали и теперь он c {} ногами'.format(dog2.name, dog2.get_legs()))
