#!/usr/bin/python3
'''Defines a class called Rectangle'''


class Rectangle:
    '''Defines properties of a rectangle'''

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if not self.__width or not self.__height:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if not self.__width or not self.__height:
            return ''
        for i in range(self.area()):
            if i and not (i % self.__width):
                print()
            print('#', end='')
        return ''

    def __repr__(self):
        a = str(self.__width)
        b = str(self.__height)
        return "Rectangle (" + a + ", " + b + ")"

    def __del__(self):
        print("Bye rectangle...")
