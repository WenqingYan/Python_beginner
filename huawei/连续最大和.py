#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Huawei 连续最大和'
__author__ = 'wenqingy'

n = int(input())
list = [*map(int, input().split())]
max = -0x8000000
for i in range(n):
    for j in range(i,n+1):
        m = sum(list[i:j+1])
        if m > max:
            max = m
print(max)

#nowcoder
n = input()
nums = input()
nums = list(map(int, nums.split()))
maxsum = -0x8000000
cursum = 0
for i in nums:
    cursum += i
    if cursum > maxsum: maxsum = cursum
    if cursum < 0: cursum = 0
print(maxsum)