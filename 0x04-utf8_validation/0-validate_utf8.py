#!/usr/bin/python3
"""the `0-validate_utf8` module
defines the function `validUTF8`
"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    encoding = []
    for char in data:
        # trim 0b from the string
        byte = bin(char).replace("0b", "")
        if len(byte) > 8:
            # 8 LSB
            byte = byte[-8:]
        encoding.append(byte)
    encoding_str = "-".join(encoding)
    return "00000000" in encoding_str
