#!/usr/bin/python3
"""
Module return representation jsan by string
"""


import json


def from_json_string(my_str):
    """
    return representation jsan by string
    """
    return json.loads(my_str)
