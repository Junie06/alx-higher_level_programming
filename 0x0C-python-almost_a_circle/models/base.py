#!/usr/bin/python3
'''Defines a class Base'''


class Base:
    """Defines the super class of classes in this directory"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructs the class

        Args:
        id(int): id parameter

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
