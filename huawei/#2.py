#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Huawei 计算字符个数'
__author__ = 'wenqingy'

class Solution(object):
    def __init__(self, astr, tag):
        self.astr = astr.lower()
        self.tag = tag.lower()

    def countTag(self):
        count = 0
        for i in self.astr:
            if i == self.tag:
                count +=1
        return count

#test
a = Solution('ABcdea 12', 'a')
a.countTag()



