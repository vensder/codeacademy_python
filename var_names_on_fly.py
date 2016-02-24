#!/usr/bin/env python3

var = 'myvar'

for i in range(4):
    exec(var+str(i) + ' = 42 +' + str(i))

for i in range(4):
    print(i)
    exec('print(' + 'myvar' + str(i) + ')')

###

mydict = {}

for i in range(4):
    keyword = var + str(i)
    mydict[keyword] = 42 + i

print(mydict)
