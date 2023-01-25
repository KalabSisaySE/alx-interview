#!/usr/bin/python3
"""the `0-validate_utf8` module
defines the function `validUTF8`
"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    for char in data:
        if len(bin(char).replace('0b', '')) > 8:
            return False
    return True
