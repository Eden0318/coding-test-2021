#Q2

data=map(int,input())
result = 0

for i in data:
    if i<=1 or result<=0:
        result+=i
    else:
        result*=i

print(result)
