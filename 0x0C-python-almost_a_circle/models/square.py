#!/usr/bin/python3
"""Defines a class Square"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """Defines the class Square"""

    def __init__(self, size, x=0, y=0, id=None):
    """Instantiates the attributes of class square"""
    super().__init__(size, x, y, id)

    @property
    def size(self):
        """gets and sets the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def to_dictionary(self):
        """returns the dictionary representation of the Square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """returns the string representation of a Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
