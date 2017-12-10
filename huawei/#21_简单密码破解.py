#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Huawei 简单密码 '
__author__ = 'wenqingy

def changeLower(x):
    if x in ['a','b','c']:
        return '2'
    elif x in ['d','e','f']:
        return '3'
    elif x in ['g','h','i']:
        return '4'
    elif x in ['j','k','l']:
        return '5'
    elif x in ['m','n','o']:
        return '6'
    elif x in ['p','q','r','s']:
        return '7'
    elif x in ['t','u','v']:
        return '8'
    else:
        return '9'

def changeUpper(x):
    upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A']
    for i in range(27):
        if x == upper[i]:
            return upper[i+1].lower()
        else:
            continue

x = input()
new = ''
for i in x:
    if i.islower():
        j = changeLower(i)
    elif i.isupper():
        j = changeUpper(i)
    else:
        j = i
    new += j
print(new)
