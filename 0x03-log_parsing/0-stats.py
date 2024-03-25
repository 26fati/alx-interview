#!/usr/bin/python3
"""Log parsing"""


def print_line(dect, size):           
    print(f"File size: {size}")
    for key, value in dect.items():
        if value != 0:
            print(f"{key}: {value}")


from sys import stdin
errors = []
count  = 0
size = 0
stats = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
try:
    for line in stdin:
        line_parsed = line.split()[::-1]
        if len(line_parsed) > 2:
            count += 1
            status = line.split(' ')[7]
            number = int(line.split(' ')[8])
            size += number
            for key, value in stats.items():
                if status == key:
                    stats[key] = value + 1
            if count == 10:
                print_line(stats, size)
                count = 0
        
finally:
    print_line(stats, size)





