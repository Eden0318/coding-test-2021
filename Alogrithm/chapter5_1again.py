num,m=map(int,input().split())
num=list(map(int,str(num)))
stack=[]

for x in num: #5276823
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)

if m!=0:
    stack=stack[:-m]

for x in stack:
    print(x,end="")