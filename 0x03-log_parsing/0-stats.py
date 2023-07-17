#!/usr/bin/python3

""" 
script that reads stdin line by line and computes metrics
"""
import sys

statusCode = ['200', '301', '400', '401', '403', '404', '405', '500']
total_file_size = 0
newObj = dict.fromkeys(statusCode, 0)

def evaluation():
    print("File size: {}".format(total_file_size))
    for key, value in sorted(newObj.items()):
        if value > 0:
            print("{}: {}".format(key, value))
            

count = 0
try:
    for line in sys.stdin:
        line = line.split()
        count += 1
        try:
            total_file_size += int(line[-1])
            if line[-2] in statusCode:
                newObj[line[-2]] += 1
        except (IndexError, ValueError):
            pass
        
        if count % 10 == 0:
            evaluation()
except KeyboardInterrupt:
    evaluation()
    raise
else:
    evaluation() 
