#!/usr/bin/python3
"""Returns Json stream"""
import json


def to_json_string(my_obj):
    """
    retuens the JSON representation of an object (string)
    """

    return json.dumps(my_obj)
