#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Huawei 字符串分隔'
__author__ = 'wenqingy'

x = input()
l = []
for i in range(len(x)-1,-1,-1):
    if x[i] not in l:
        l.append(x[i])
new = sum(l)
print(int(new))

#newcode
n=raw_input()
l=list(reversed(n))#反向遍历
result=[]
for i in l:
    if i not in result:
        result.append(i)
print("".join(result))#合并字符串
