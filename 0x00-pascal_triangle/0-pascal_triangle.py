#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""

def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []
    lst = []
    for i in range(n):
        mini_list = [1]
        if i > 0:
            prev = lst[i - 1]
            for j in range(1, len(prev)):
                x = prev[j] + prev[j - 1]
                mini_list.append(x)
            mini_list.append(1)
        lst.append(mini_list)
    return lst
