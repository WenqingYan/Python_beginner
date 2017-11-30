#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Huawei 明明的随机数'
__author__ = 'wenqingy'

class Solution(object):
    def __init__(self, n, list):
        self.n = n
        self.list = list

    def removeRank(self):
        output = []
        for i in list:
            if i not in output:
                output.append(i)
            else:
                continue
        return sorted(output)

#test
n = 5
list = [1, 2, 3, 4, 4]
a = Solution(n, list)
b = a.removeRank()
for i in b:
    print(i)


#newcoder
while True:
    try:
        n = int(input()) #输入数据的个数
        result = set()
        for i in range(n):
            result.add(int(input()))#输入相应的数据
        
        sortres = sorted(list(result))
        for i in sortres:
            print(i)
    except:
        break



