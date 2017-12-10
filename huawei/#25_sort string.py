#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Huawei 字符串排序'
__author__ = 'wenqingy

a = input()
b=[i for i in a.strip()]
alpha = list(filter(lambda x: x.isalpha(), b))
alpha.sort(key = lambda x: x.lower())

j = 0
for i in range(len(b)):
    if b[i].isalpha():
        b[i] = alpha[j]
        j += 1

print(''.join(b))#采用strip分割所以结尾的时候采用‘’空来合并list中的各个元素

