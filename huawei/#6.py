#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Huawei 质数因子'
__author__ = 'wenqingy'

#直接输出质数因子
x = int(input())
for a in range(2,x+1):
    if x % a != 0:
        a += 1
    else:
        print(a, end=' ')
        x = x // a

#有重复的输出质数因子
x = int(input())
a = 2
while x != 1:
    if x % a == 0:
        print(a, end=' ')
        x = x // a
    else:
        a += 1




