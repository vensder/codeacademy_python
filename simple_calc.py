#!/usr/bin/env python3
# -*- coding:utf-8 -*-

n1 = n2 = 0

def input_numbers(n1,n2):
    print('Input first number:')
    n1 = float(input())
    print('Input second number:')
    n2 = float(input())
    return(n1,n2)

while True:
    print('Choice action ("+", "-", "*" or "/":)')
    op = input()

    if op == '+':
        n1,n2 = input_numbers(n1,n2)
        print(str(n1) + ' + ' + str(n2) + ' = ' + str(n1 + n2))
    else:
        break



