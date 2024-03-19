#!/usr/bin/env python3
""" method that calculates the fewest number of operations
needed to result in exactly n H characters in the file."""


def minOperations(n):
    """calculates the fewest number of operations
    needed to result in exactly n H characters
    """
    sum = 0
    divisor = 2
    if n < 0:
        return 0
    while divisor <= n:
        if n % divisor == 0:
            sum += divisor
            n = n / divisor
        else:
            divisor += 1

    return sum
