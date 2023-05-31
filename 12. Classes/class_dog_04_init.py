#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Dog: # класс
    def __init__(self, name, head, body, legs, tail): # конструктор класса
        self.name = name
        self.legs = legs
        self.head = head
        self.body = body
        self.tail = tail
        if self.tail:
            self.tail_str = 'с хвостом'
        else:
            self.tail_str = 'без хвоста'

        print('На свет появился {} c {} ногами и {}'.format(self.name, self.legs, self.tail_str))

dog1 = Dog('Шарик', 1, 1, 4, True)
dog2 = Dog('Барбос', 1, 1, 3, False)
dog2.legs = 4
dog2.tail = True
print('Собаку по кличке {} прооперировали и теперь он c {} ногами и {}'.format(dog2.name, dog2.legs, dog2.tail_str))

