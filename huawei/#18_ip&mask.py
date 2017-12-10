#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Huawei 识别IP Netmask '
__author__ = 'wenqingy'

def classify(ip):
    a = ip.split('.')[0]
    a = int(a)
    if a in range(0,128):
        return 0
    elif a in range(128,192):
        return 1
    elif a in range(192,224):
        return 2
    elif a in range(224,240):
        return 3
    elif a in range(240,256):
        return 4
    else:
        return 5




def checkMask(mask):
    num = [129,192,224,240,248,252,254]
    if checkIp(mask) == 0:
        m = [*map(int, mask.split('.'))]
        flag = 0
        #找出中间的不为的数一分为二
        for i in range(4):
            if m[i] != 255 and m[i] != 0 and m[i] in num:
                for j in range(i):
                    if m[j] != 255:
                        return 1
                for j in range(i+1,4):
                    if m[j] != 0:
                        return 1
                    else:
                        return 0
            else:
                flag += 1

        if flag == 4:
            if (m[0] == 255 and sum(m[1:4]) == 0) or (m[0] == 255 and m[1] == 255 and sum(m[2:4]) == 0) or (m[0] == 255 and m[1] == 255  and m[2] == 255 and sum(m[3:4]) == 0):
                return 0
            else:
                return 1
    else:
        return 1

def checkIp(ip):
    p = ip.split('.')
    #print(p)
    if len(p) == 4:
        for i in p:
            # 切分字符之后 没有的部分变为 ‘’ 而不是None
            if i == '' or i == ' ':
                return 1
            elif int(i) not in range(0,256):
                return 1
        return 0
    else:
        return 1

def private(ip):
    ip = [*map(int, ip.split('.'))]
    if ip[0] == 10:
        return 1
    elif ip[0] == 172 and ip[1] in range(16,32):
        return 1
    elif ip[0] == 192 and ip[1] == 168:
        return 1
    else:
        return 0

# 3.6 修改
m = '255.255.255.0'
type(m.split('.'))
[*map(int, m.split('.'))]

m = '255'
print(checkMask(m))

m = '255.254.27.255'
print(classify(m))

output = [0]*7
while True:
    string = input()
    if string == '':
        break
    ip = string.split('~')[0]
    mask = string.split('~')[1]
    if checkIp(ip) == 0 and checkMask(mask) == 0:
        i = classify(ip)
        if i != 5:
            output[i] += 1
            j = private(ip)
            output[6] += j      
    else:
        output[5] += 1

for i in output:
    print(i, end = ' ')

print ("%s %s %s %s %s %s %s" %(output[0],output[1],output[2],output[3],output[4],output[5],output[6]))