#!/usr/bin/env python3
"""
 Basic Serialization module
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialisation module
    """
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Deserialization module
    Return data
    """
    with open(filename, "r") as f:
        data = json.load(f)
    return data
