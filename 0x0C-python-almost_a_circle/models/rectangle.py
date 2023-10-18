#!/usr/bin/python3
"""Defines class Rectangle that inherits from super class Base"""

from models.base import Base


class Rectangle(Base):
    """Defines a subclass Rectangle that initializes the properties
    of a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args:
            width(int, float): width of a rectangle
            height(int, float): height of a rectangle
            x(int, float)
            y(int, float)
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """gets the attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """validates instantiation"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """gets the attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """validates instantiation"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gets the attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """validates instantiation"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """gets the attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """validates instantiation"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value  < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area value of a rectangle"""
        return self.width * self.height

    def display(self):
        """Prints to standard output the display of the character #"""
        for i in range(self.height)
        print('#' * self.width)
