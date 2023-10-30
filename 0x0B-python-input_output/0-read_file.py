#!/usr/bin/python3
"""Reads a text file and prints it"""


def read_file(filename=""):
    """
    Reads a text file
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
