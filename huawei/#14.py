#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Huawei 字串的连接最长路径'
__author__ = 'wenqingy'

# 为何用set不能过测试
n = int(input())
l = set()
for i in range(n):
    l.add(input())
for j in l:
    print(j)
   
