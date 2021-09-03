num,m=map(int,input().split())
num=list(map(int,str(num)))
stack=[] #9

for x in num:  #9977252641 5
    while stack and 0<m and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)

if m!=0:
    stack=stack[:-m]

for x in stack:
    print(x, end='')


