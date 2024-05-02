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
        total (int): The total i for which change needs to be made.

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
    for coin in coins:
        for i in range(coin, total + 1):
            array[i] = min(array[i], array[i - coin] + 1)

    if math.isinf(array[-1]):
        return -1
    return array[-1]
