#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def input_to_float(text):
    n = None
    while n is not float:
        try:
            print(text)
            n = float(input())
            return n
        except ValueError:
            print('Wrong number format')

def input_numbers():
    n1 = input_to_float('Input first number:')
    n2 = input_to_float('Input second number:')
    return(n1,n2)

while True:
    print('Choice action ("+", "-", "*" or "/":)')
    op = input()

    n1 = n2 = 0
    if op == '+':
        n1,n2 = input_numbers()
        print(str(n1) + ' + '  + str(n2) + ' = ' + str(n1 + n2))
    else:
        break



