#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

if __name__ == "__main__":
  boxes = [[1, 4, 5], [2], [5, 2], [3], [4, 1], [3, 5]]
  print(canUnlockAll(boxes))