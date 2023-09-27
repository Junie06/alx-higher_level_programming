#!/usr/bin/python3
'''This module defines a class'''


class Square:
    '''This class defines the attributes of Square and checks for exceptions'''

    def __init__(self, size=0):
        '''Args:
            size (int): size of object
        '''

        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
