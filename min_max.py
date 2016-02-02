#!/usr/bin/env python
# -*- coding: utf-8 -*-

def string_to_num(num):
    try:
        return int(num)
    except ValueError:
        return float(num)

def biggest_number(*args):
    return max(args)
    
def smallest_number(*args):
    return min(args)

def distance_from_zero(arg):
    return abs(arg)


a = raw_input("Input first number:\n")
b = raw_input("Input second number:\n")
c = raw_input("Input third number:\n")
d = raw_input("Input fourth number:\n")

a = string_to_num(a)
b = string_to_num(b)
c = string_to_num(c)
d = string_to_num(d)

print 'Results:'
print 'The biggest number is: ' + str(biggest_number(a, b, c, d))
print 'The smallest number is: ' + str(smallest_number(a, b, c, d))
print 'Distance from zero of the first number is: %s' % distance_from_zero(a)
