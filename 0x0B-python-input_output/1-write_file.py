#!/usr/bin/python3
"""Writes to a text file"""
import json


def write_file(filename="", text=""):
    """
    writes a string to a text file
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
