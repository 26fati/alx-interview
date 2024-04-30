#!/usr/bin/python3
"""
Main file for testing
"""
import time
makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

print(makeChange([], 1))
start = time.time()

for i in range(10):
    makeChange([2, 4, 6, 10], 1278653)

end = time.time()

avg = (end - start) / 10

if avg > 3:
    print("Runtime too long")
else:
    print("OK")
