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
        return len(output),sorted(output)

#test
n = 5
list = [1, 2, 3, 4, 4]
a = Solution(n, list)
a.removeRank()



