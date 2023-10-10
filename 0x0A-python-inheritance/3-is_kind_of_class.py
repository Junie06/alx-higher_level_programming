#!/usr/bin/python3
"""Defines a class and inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance or inherited instance of a clas

    Args:
        obj (any): The object
        a_class (type): The class to match the type of obj to check
    Returns:
        If obj is an instance or inherited instance of a_class - True
        Else - False
    """
    if isinstance(obj, a_class):
        return True
    return False
