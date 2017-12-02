num = ['0','1','2','3','4','5','6','7','8','9']
direction = ['A', 'S', 'W', 'D']
path = input().split(';')
x = 0
y = 0
for p in path:
    if len(p) > 3 or len(p) == 0:
        continue
    else:
        if p[0] in direction:
                if len(p) == 2:
                    if p[1] in num:
                        pass
                    else:
                        continue
                elif len(p) == 3:
                    if p[1] in num and p[2] in num:
                        pass
                    else:
                        continue
                move = int(p[1:])
                if p[0] == 'A':
                    x -= move
                elif p[0] == 'D':
                    x += move
                elif p[0] == 'W':
                    y += move
                else:
                    y -= move
        else:
            continue
print(str(x)+','+str(y))

#newcoder
while True:
    try:
        s=input().split(';')
        line=[]
        for i in s:
            if len(i)<=3 and i[1:].isdigit(): #is.. function
                line.append(i)
        x=0
        y=0
        for item in line:
            if item[0]=='A':
                x=x-int(item[1:])
            if item[0]=='D':
                x=x+int(item[1:])
            if item[0]=='W':
                y=y+int(item[1:])
            if item[0]=='S':
                y=y-int(item[1:])
        print(str(x)+','+str(y))
    except:
        break