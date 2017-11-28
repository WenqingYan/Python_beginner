#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'No.476 in leekcode'
__author__ = 'wenqingy'

class Solution(object):
    def __init__(self, num):
        self.num = num

    def findComplement(self):
        num = str(bin(self.num))
        rev = ''
        for n in range(len(num)):
            if n > 1:
                rev += str(int(num[n])^1)
        return int(rev, base=2)

#test
 a = Solution(5)
 a.findComplement()

 b = Solution(1)
 b.findComplement()
