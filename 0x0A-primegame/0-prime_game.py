#!/usr/bin/python3
"""summary
"""


def get_primes(n):
    """Return list of prime numbers between 1 and n inclusive

    Args:
        n ([type]): [description]

    Returns:
        [type]: [description]
    """
    primes = []
    prime = [True for i in range(n+1)]
    for p in range(2, n + 1):
        if (prime[p]):
            for i in range(p * p, n+1, p):
                prime[i] = False
            primes.append(p)
        p += 1
    return primes


def isWinner(x, nums):
    """Determines winner of Prime Game

    Args:
        x ([type]): [description]
        nums ([type]): [description]

    Returns:
        [type]: [description]
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        primes = get_primes(nums[i])
        if len(primes) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Ben > Maria:
        return 'Ben'
    elif Maria > Ben:
        return 'Maria'
    else:
        return None
