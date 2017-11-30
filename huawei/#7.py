#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Huawei 质数因子'
__author__ = 'wenqingy'

x = input()
for i in range(len(x)):
    if x[i] == '.':
        tag = i;
        break
if int(x[tag+1]) < 5:
    x = float(x) // 1
else:
    x = float(x) //1 + 1
print(int(x))

#newcode
a=float(input())
print(round(a+0.001)# 对于4.5一类的数字round会舍变4  在后面加上一个无关紧要的0.001 但是遇到4.49仍然会出错
