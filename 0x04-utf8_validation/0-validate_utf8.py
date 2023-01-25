#!/usr/bin/python3
"""the `0-validate_utf8` module
defines the function `validUTF8`
"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    encoding = []
    # convert data to binaries
    for char in data:
        # trim 0b from the string
        byte = bin(char).replace("0b", "")
        if len(byte) > 8:
            # only the 8 LSB ignore the rest
            byte = byte[-8:]
        elif len(byte) < 8:
            # to get an 8-bit string for each data
            prefix = '0' * (8 - len(byte))
            byte = prefix + byte
        encoding.append(byte)
    indexes_with_10 = []
    i = 0

    # collect indexs that need to start with '10'
    while i < len(data):
        if encoding[i].startswith('1'):
            # the numbers '1's until the first 0
            nb_of_bytes = encoding[i].index('0')
            if nb_of_bytes > 4:
                return False
            indexes_with_10.extend(range(i + 1, i + nb_of_bytes))
            # jump to the next new characther
            i = i + nb_of_bytes
        else:
            i = i + 1
    # print(nb_of_bytes)

    for index in indexes_with_10:
        if not encoding[index].startswith('10'):
            return False
    return True
