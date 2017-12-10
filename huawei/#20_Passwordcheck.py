#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Huawei 密码验证合格程序 '
__author__ = 'wenqingy'

def checkLen(s):
    if len(s) > 8:
        return 1
    else:
        return 0

def check3in4(s):
    l = [0]*4
    for i in s:
        if i.islower():
            l[0] = 1
        elif i.isupper():
            l[1] = 1
        elif i.isdigit():
            l[2] = 1
        else:
            l[3] = 1
    if sum(l) >= 3:
        return 1
    else:
        return 0

#用count来检验子串重复性
def checkRep(s):
    for i in range(len(s)-3):
        if s.count(s[i:i+3]) > 1:
            return 0
    return 1

while True:
    try:
        x = input().strip()
        if checkLen(x) == 1 and checkRep(x) == 1 and check3in4(x) == 1:
            print('OK')
        else:
            print('NG')
    except:
        break
