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

