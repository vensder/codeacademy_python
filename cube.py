#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt

def cube(number):
    return number ** 3
    

def by_three(number):
    if (number % 3) == 0:
        print cube(number)
    else:
        print "False"

number = int(raw_input("Enter number:\n"))

by_three(number)

print sqrt(number)
