#!/usr/bin/python3
'''This module defines a class called Square'''


class Square:
    '''This class is defined with attributes, raises errors
        and return area of the square
    '''

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        return (pow(self.__size, 2))

    def my_print(self):
        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
