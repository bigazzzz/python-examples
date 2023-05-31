#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Инкапсуляция
'''
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

    def set_legs(self, legs):
        if 0<=legs<=4:
            self.legs = legs
        else:
            print('Ног должно быть от 0 до 4')

    def get_legs(self):
        return self.legs

    def set_tail(self, tail):
        self.tail = tail
        if self.tail:
            self.tail_str = 'с хвостом'
        else:
            self.tail_str = 'без хвоста'



dog1 = Dog('Шарик', 1, 1, 4, True)
dog2 = Dog('Барбос', 1, 1, 3, False)
dog2.set_legs(4)
dog2.set_tail(True)
print('Собаку по кличке {} прооперировали и теперь он c {} ногами и {}'.format(dog2.name, dog2.legs, dog2.tail_str))

