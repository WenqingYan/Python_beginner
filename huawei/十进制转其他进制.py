#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Huawei 十进制转其他进制'
__author__ = 'wenqingy'

num = '0123456789ABCDEFGHIJKMLNOPQRSTUVWXYZ'
m,n = map(int, input().split())
result = ''
sign = ''
if m < 0:
    sign = '-'
    m = -m
while m > n:
    result = num[m%n] + result #左加新的余数
    m = m // n
result = num[m] + result
result = sign + result
print(result)