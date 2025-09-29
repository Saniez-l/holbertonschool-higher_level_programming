#!/usr/bin/python3
"""
Module for return represnetation json
"""


import json


def to_json_string(my_obj):
    """
    Return representation json
    """
    x = my_obj
    json.dumps(x)
    return x
