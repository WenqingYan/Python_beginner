#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Huawei 购物单'
__author__ = 'wenqingy'

# 用二进制暴力循环
N, m = map(int, input().split())
v = []
w = []
q = []
for i in range(m):
    a, b, c = map(int, input().split())
    v.append(a)
    w.append(b)
    q.append(c)
    
imp = 0
for j in range(1, 2**m):
    buy = []
    i = bin(j)
    for n in range(1, len(i)-1):
        a = int(i[-n])
        if a == 1:
            buy.append(n-1)
            if q[n-1] != 0:
                buy.append(q[n-1])
    
    buy = set(buy)
    impn = 0
    money = 0
    for s in buy:
        money += v[s]
        impn += v[s]*w[s]
        
    if money <= N:
        if impn > imp:
            imp = impn
            for s in buy:
                print(s, end=' ')

    else:
        continue

print(imp)

#newcoder
N, m = map(int, input().split())
goods = []
for i in range(m):
    goods.append(list(map(int,input().split()))) # 

bag = [[0]*(N+1) for _ in range(m+1)]

for i in range(1,m+1):
    for j in range(1,N+1):
        if goods[i-1][2] == 0:
            if goods[i-1][0] <= j:
                bag[i][j] = max(bag[i-1][j], bag[i-1][j-goods[i-1][0]]+goods[i-1][0]*goods[i-1][1])
            else:
                # 不知道应该如何写
                if goods[i-1][0]+goods[goods[i-1][2]-1][0] <= j:
                    bag[i][j] = max(bag[i-1][j])

print(bag[m][N])