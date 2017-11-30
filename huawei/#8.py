#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Huawei 合并表记录'
__author__ = 'wenqingy'


while True:
    try:
        n = int(input())
        dic = {}
        for i in range(n):
            k, v = map(int, input().split())
            if k in dic:
                dic[k] += v
            else:
                dic[k] = v
            
        for (i, j) in dic.items():
            print(i,j)
    except:
        break




