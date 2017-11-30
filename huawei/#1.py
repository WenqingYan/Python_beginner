#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Huawei 字符串最后一个单词'
__author__ = 'wenqingy'

class Solution(object):
    def __init__(self, astr):
        self.astr = astr

    def checkLast(self):
        for i in range(len(self.astr)-1,0,-1):
            if self.astr[i] != ' ':
                last = i
                break
            else:
                continue

        for j in range(last,-1,-1):
            if self.astr[j] == ' ':
                flag = j
                break
            elif j == 0:
                flag = -1

        return last - flag

#test
#a = Solution('Today is a new start')
#b = Solution('Today is a new start                  ')
#a.checkLast()
#b.checkLast()

# input part
def main():
    a = input('Please input new data:\n')
    b = Solution(a)
    print(b.checkLast())

# main function for testing
main()

#newcoder
x = input()
for i in range(len(x)-1, -1, -1):
    if x[i] == ' ':
        break
    elif i == 0:
        i = -1
print(len(x)-i-1)