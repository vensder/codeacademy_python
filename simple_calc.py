#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def print_name():
    print(__name__)

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
    '''input numbers

    You should input float number.
    Caution: if you enter bad value this function never stops. Ahahahah!
    '''
    n1 = input_to_float('Input first number:')
    n2 = input_to_float('Input second number:')
    return(n1,n2)

def print_answer(n1,n2,op,result):
    print(str(n1) + op + str(n2) + ' = ' + str(result))

if __name__ == "__main__":
    while True:
        oplist = ['+','-','*','/']
        op = None
        while op not in oplist:
            print('Choice action ("+", "-", "*" or "/":)')
            op = input()
        n1, n2 = input_numbers()
        result = 0
        if op == '+':
            result = n1 + n2
        elif op == '-':
            result = n1 - n2
        elif op == '*':
            result = n1 * n2
        elif op == '/':
            try:
                result = n1 / n2
            except ZeroDivisionError:
                print('Division by Zero')
        else:
            break

        print_answer(n1,n2,op,result)
