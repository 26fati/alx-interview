#!/usr/bin/python3
'''
    a script that determines if a
    given data set represents a valid UTF-8 encoding.
'''


def validUTF8(data):
    ''' a method that determines if a given
    data set represents a valid UTF-8 encoding.'''
    byte = 1
    for num in data:
        if byte == 1:
            if (num >> 5) == 0b110:
                byte = 2
            elif (num >> 4) == 0b1110:
                byte = 3
            elif (num >> 3) == 0b11110:
                byte = 4
            elif (num >> 7):
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            byte -= 1
    return byte == 1
