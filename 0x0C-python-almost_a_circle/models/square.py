#!/usr/bin/python3
"""Defines a class Square"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """Defines the class Square"""

    def __init__(self, size, x=0, y=0, id=None):
    """Instantiates the attributes of class square"""
    super().__init__(size, x, y, id)
