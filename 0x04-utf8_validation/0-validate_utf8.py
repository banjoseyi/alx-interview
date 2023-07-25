#!/usr/bin/python3

""" 
Method that determines if a given data set represents
a valid UTF-8 encoding.
"""

def validUTF8(data):
    number_of_bytes = 0
    
    for x in data:
        if number_of_bytes == 0:
            if x >> 5 == 0b1110 or x >> 5 == 0b110:
                number_of_bytes = 1
            elif x >> 4 == 0b1110:
                number_of_bytes = 2
            elif x >> 3 == 0b11110:
                number_of_bytes = 3
        else:
            if x >> 6 != 0b10 or x >> 7 == 0b1:
                return False
            number_of_bytes -= 1
    return number_of_bytes == 0
