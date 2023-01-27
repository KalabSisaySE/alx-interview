#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

if __name__ == "__main__":
    boxes = [
        [10, 3, 8, 9, 6, 5, 8, 1],
        [8, 5, 3, 7, 1, 8, 6],
        [5, 1, 9, 1],
        [],
        [6, 6, 9, 4, 3, 2, 3, 8, 5],
        [9, 4],
        [4, 2, 5, 1, 1, 6, 4, 5, 6],
        [9, 5, 8, 8],
        [6, 2, 8, 6]
    ]

    print(canUnlockAll(boxes))
