#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
def tax(bill):
    bill *= 1.08
    print "With tax: %f" % bill
    return bill
    
def tip(bill):
    bill *= 1.15
    print "With tip: %f" % bill
    return bill
   
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)
'''

def one(n):
    return n + 1
    
def two(n):
    return one(n) + 2
    print n

n = 1    
n = one(n)
print n
n = two(n)
print n
