#!/usr/bin/python3
"""the `0-validate_utf8` module
defines the function `validUTF8`
"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    if type(data) is list and len(data) > 0:
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
                try:
                    nb_of_bytes = encoding[i].index('0')
                    if nb_of_bytes > 4:
                        return False
                    if i + 1 == i + nb_of_bytes:
                        indexes_with_10.extend(
                            range(i + 1, i + nb_of_bytes + 1)
                        )
                    else:
                        indexes_with_10.extend(range(i + 1, i + nb_of_bytes))
                    # jump to the next new characther
                    i = i + nb_of_bytes
                except ValueError:
                    return False
            else:
                i = i + 1
        # print(nb_of_bytes)
        for index in indexes_with_10:
            try:
                if not encoding[index].startswith('10'):
                    return False
            except IndexError:
                return False
        return True
    else:
        return False
