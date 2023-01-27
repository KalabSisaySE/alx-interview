#!/usr/bin/python3
import random

canUnlockAll = __import__('0-lockboxes').canUnlockAll

if __name__ == "__main__":
    boxes = [
        [7, 5],
        [1, 10, 7],
        [9, 6, 10],
        [7, 9],
        [2],
        [7, 3],
        [7, 9, 10, 10, 8, 9, 2, 5],
        [7, 2, 2, 4, 4, 2, 4, 8, 7],
        [4, 2, 9, 6, 6, 5, 5],
    ]

    print(canUnlockAll(boxes))