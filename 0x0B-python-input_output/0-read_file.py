#!/usr/bin/python3
"""Reads a text file"""
import json


def read_file(filename=""):
    """
    Reads a text file
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end"")
