#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Huawei 兄弟单词'
__author__ = 'wenqingy
words = input().split()
candi = []
for i in range(int(words[0])):
    if words[-2] != words[i+1] and sorted(words[-2]) == sorted(words[i+1]):
        candi.append(words[i+1])
candi.sort()
print(len(candi))
if len(candi) >= int(words[-1]):
    print(candi[int(words[-1])-1])