#!/usr/bin/python3
"""Defines a function that determines if a box containing a list
   of lists can be opened using keys
"""


def canUnlockAll(boxes):
    """return trure if all boxes unlocked"""
    visited = [0]
    queue = [0]
    while queue:
        index = queue[0]
        for number in boxes[index]:
            if number not in visited:
                visited.append(number)
                queue.append(number)
        queue.pop(0)
    return (len(boxes) == len(visited))
