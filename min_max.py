#!/usr/bin/env python
# -*- coding: utf-8 -*-

def string_to_num(num):
    try:
        return int(num)
    except ValueError:
        return float(num)

def biggest_number(arg):
    return max(arg)
    
def smallest_number(arg):
    return min(arg)

def distance_from_zero(arg):
    return abs(arg)

n = 4
i = 0
collection = [None] * n

for i in range (0, n):
    collection[i] = raw_input("Input number:\n")

print collection

collection = [string_to_num(n) for n in collection]
print collection

print 'Results:'
print 'The biggest number is: ' + str(biggest_number(collection))
print 'The smallest number is: ' + str(smallest_number(collection))
print 'Distance from zero of the first number is: %s' % distance_from_zero(collection[0])
