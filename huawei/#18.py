#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Huawei 识别IP Netmask '
__author__ = 'wenqingy'

def classify(ip):
    a = ip.split('.')[0]
    a = int(a)
    if a in range(1,128):
        return 0
    elif a in range(128,192):
        return 1
    elif a in range(192,224):
        return 2
    elif a in range(224,240):
        return 3
    elif a in range(240,256):
        return 4

def checkMask(mask):
    num = [129,192,224,240,248,252,254,255]
    m = mask.split('.')
    if len(m) = 4 and m[0] in num and m[1] in num and m[2] in num and m[3] in num:
        return 0
    else:
        return 1
    
def checkIp(ip):
    if len(ip)
        
output = [0]*7
while True:
    string = input()
    if string == '':
        break
    ip = string.split('~')[0]
    mask = string.split('~')[1]
    
