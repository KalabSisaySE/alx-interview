#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

if __name__ == "__main__":
  boxes = [[0]]
  print(canUnlockAll(boxes))