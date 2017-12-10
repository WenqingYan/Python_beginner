#注 测试用例保证输入参数的正确性，测试用例不止一组
#输入多行 输出多行
#或者题目提示说没有进行多case处理，则用while True
while True:
    try:
        n = int(input()) #输入数据的个数
        result = set()#去重储存
        for i in range(n):
            result.add(int(input()))#输入相应的数据
  
        sortres = sorted(list(result))
        for i in sortres:
            print(i)
    except:
        break

#多个对象， 一个对象多个属性
N,m = map(int,raw_input().split())
goods = []
for i in range(m):
    goods.append(list(map(int,raw_input().split())))
goods[0][0]#第一个对象的第一个属性


#多个输入 同行用空格隔开
while True:
    try:
        n = int(input())
        dic = {}
        for i in range(n):
            k, v = map(int, input().split())
            if k in dic:
                dic[k] += v
            else:
                dic[k] = v
            
        for (i, j) in dic.items():
            print(i,j)
    except:
        break

#实例中 单次输入输出
x = intput()
pass
print()

#多次输入, 题目中’接受一个..和一个..
x = input()
y = intput()

a = set()
a.add('hello')
a.add('cristina')
a
for i in a:
    print(i)


#多个数据输入不预先给出数据个数
#题目未给出个数，每个数据一行，未提及终止输入的方法
while True:
    string = input()
    if string == '':#enter enter 两次则退出
        break
    pass

#也可以直接写单个的
while True:
    try:
        input
        print
        pass
    except:
        break
