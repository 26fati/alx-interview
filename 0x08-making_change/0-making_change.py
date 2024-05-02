#!/usr/bin/python3
'''
a script that Calculates the minimum number
of coins needed to make change for a given total.
'''
import math


def makeChange(coins, total):
    """
    Calculates the minimum number of coins
    needed to make change for a given total.

    Args:
        coins (list): A list of coin denominations available.
        total (int): The total amount for which change needs to be made.

    Returns:
        int: The minimum number of coins needed
        to make change for the given total.
             Returns -1 if it is not possible
             to make change for the given total.

    """
    if total <= 0:
        return 0
    array = [float('inf')] * (total + 1)
    array[0] = 0
    for p in range(1, total + 1):
        for i in range(len(coins)):
            if coins[i] <= p:
                array[p] = min(1 + array[p - coins[i]], array[p])

    if math.isinf(array[-1]):
        return -1
    return array[-1]
