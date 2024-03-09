#!/usr/bin/python3

def pascal_triangle(n):
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
