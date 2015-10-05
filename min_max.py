#!/usr/bin/env python
# -*- coding: utf-8 -*-

def biggest_number(*args):
    return max(args)
    
def smallest_number(*args):
    return min(args)

def distance_from_zero(arg):
    return abs(arg)


print biggest_number(-10, -5, 5, 10)
print smallest_number(-10, -5, 5, 10)
print distance_from_zero(-10)
