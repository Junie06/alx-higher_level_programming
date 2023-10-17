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
            return self.__width

        @property
        def height(self):
            return self.__height

        @property
        def x(self):
            return self.__x

        @property
        def y(self):
            return self.__y

        @width.setter
        def width(self, val):
            if not type(val, int):
                raise TypeError("width must be an integer")
            if width <= 0:
                raise ValueError("width must be > 0")
            self.__width = val

        @height.setter
        def height(self, val):
            if not type(val, int):
                raise TypeError("height must be an integer")
            if height <= 0:
                raise ValueError("height must be > 0")
            self.__height = val

        @x.setter
        def x(self, val):
            if not type(val, int):
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = val

        @y.setter
        def y(self, val):
            if not type(val, int):
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = val

        def area(self):
            """Calculates the area value of a rectangle"""
            return self.width * self.height

        def display(self):
            """Prints to standard output the display of the character #"""
            if self.width == 0 or self.height == 0:
                print("")
                return
            [print("") for j in range(self.y)]
        for j in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

        def __str__(self):
            """Returns the string representation of class Rectangle"""
            return "[Rectangle] {()} {}/{} - {}/{}".format(self.id, self.x,
                                                        self.y, self.width,
                                                        self.height)
