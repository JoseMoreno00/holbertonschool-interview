#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and each box may contain
keys to the other boxes.
"""


def canUnlockAll(boxes):
    keys = []
    count = 0
    many = len(boxes)
    for box in boxes:
        if count == 0:
            for value in box:
                keys.append(value)
        else:
            if count in keys:
                for value in box:
                    keys.append(value)
            else:
                temp = count
                for value in boxes[temp + 1]:
                    if temp + 1 in keys:
                        keys.append(value)
                    if temp + 1 == many:
                        return False
                    temp += 1
        count += 1
    return True
