n=list(input())
stack=[]
x=[]
for i in n:
    if i.isdigit():
        stack.append(i)
    else:
        x.append(i)

