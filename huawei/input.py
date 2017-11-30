#class Animal(object):
    #def run(self):
        #print('Animal')

class Dog(Animal):
    def run(self):
        print('Dog')

def run2(animal):
    animal.run()
    animal.run()

#test
run2(Dog())


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Huawei input'
__author__ = 'wenqingy'

# no hint
sentinel = 'end' # 遇到这个就结束
lines = []
for line in iter(input('new data:'), sentinel):
    lines.append(line)

#with hint
from functools import partial
inputNew = partial(input, 'Please input new data:\n')
sentinel = 'end' # 遇到这个就结束
lines = []
for line in iter(inputNew, sentinel):
    lines.append(line)

print(lines)

#single line
a = input('Please input new data:\n')

#mutiple varable
a, b = input().split()
print(a,b)