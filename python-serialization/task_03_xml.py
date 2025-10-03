#!/usr/bin/python3
"""
Module to serialize and deserialise xml
"""
import json
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize xml
    """
    data = ET.Element('data')

    for key in dictionary:
        ET.SubElement(data, key).text = dictionary[key]

    tree = ET.ElementTree(data)
    tree.write(filename, encoding='utf-8')


def deserialize_from_xml(filename):
    """
    Deserialise xml
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionnaire = {}
    for child in root:
        dictionnaire[child.tag] = child.text
    return dictionnaire
