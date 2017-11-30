#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Huawei 字符串分隔'
__author__ = 'wenqingy'

class Solution(object):
    def __init__(self, astr):
        self.astr = astr

    def cutString(self):
        rem = len(self.astr) % 8
        rep = len(self.astr) // 8
        newstr = self.astr + '0'*(8-rem)#没有注意8的倍数不加0的情况
        #print(newstr)
        print(type(len(newstr)))
        for r in range(len(newstr)//8):
            print(newstr[r*8:r*8+8])
        return

#test
a = Solution('abc')
a.cutString()

b = Solution('123456789')
b.cutString()

c = 'abcde'
print(c[::-1])

#newcoder
class Solution(object):
    def __init__(self, astr):
        self.astr = astr

    def cutString(self):
        rem = len(self.astr) % 8
        rep = len(self.astr) // 8
        if rem != 0:
            newstr = self.astr + '0'*(8-rem)
        else:
            newstr = self.astr
        for r in range(len(newstr)//8):#/得到的是float //才是int
                print(newstr[r*8:r*8+8])
        return
    
while True:
    try:
        x = input()
        a = Solution(x)
        a.cutString()
    except:
        break