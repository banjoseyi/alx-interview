#!/usr/bin/python3
"""
    Method that calculates the fewest number of operations 
    needed to result in exactly n H chracers in the file
"""

def minOperations(n):
   operation_count = 0
   minimum_operation = 2
   
   """while loops through each value of n"""
   while n > 1:
        while n % minimum_operation == 0:
            operation_count = operation_count + minimum_operation
            n = n / minimum_operation
        minimum_operation = minimum_operation + 1
   return operation_count
