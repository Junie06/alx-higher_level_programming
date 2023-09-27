#!/usr/bin/python3
'''This module defines a class called Square'''


class Square:
    '''This class is defined with attributes, raises errors
        and return area of the square
    '''

    def __init__(self, size=0):
            self.__size = size

    def size(self):
        return (self.__size)

    def size(self, value):
        if isinstance(size, int):
            self.__size = value
        else:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        return (pow(self.__size, 2))
