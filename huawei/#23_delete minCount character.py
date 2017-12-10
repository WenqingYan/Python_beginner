#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Huawei 删除字符串中出现次数Min的字符'
__author__ = 'wenqingy

upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

x = input()
count = [0]*26
for i in range(26):
    count[i] = x.count(lower[i])

min = 20
j = []
for i in range(len(count)):
    if count[i] < min and count[i] != 0: #没有的出现过的字母计数为0
        min = count[i]


for i in range(len(count)):
    if count[i] == min:
        j.append(i)

for i in j:
    x = x.replace(lower[i],'')
print(x)


