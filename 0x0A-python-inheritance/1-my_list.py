#!/usr/bin/python3
"""Defines an sub-class MyList."""


class MyList(list):
    """Prints sorted list for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order"""
        print(sorted(self))
