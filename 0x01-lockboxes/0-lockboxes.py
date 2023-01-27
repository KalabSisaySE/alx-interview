#!/usr/bin/python3
"""defines the function `canUnlockAll`"""


def canUnlockAll(boxes):
    """determines of all `boxes` can be unlocked"""
    keys = {0}  # boxes whose keys are found
    searched = set()  # boxes opened and searched for more keys

    while len(keys) > 0:
        key = keys.pop()
        # if key is valid and not searched
        if key < len(boxes) and key >= 0 and key not in searched:
            searched.add(key)
            for i in boxes[key]:
                # if key inside the box is valid and not searched
                if i < len(boxes) and i >= 0 and i not in searched:
                    keys.add(i)

    return searched == set(range(len(boxes)))
