#1번째 방법
n=int(input())
n_data=list(map(int,input().split()))
def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10
        x=x//10
    return sum

max=-2147000000
for x in n_data:
    total=digit_sum(x)
    if total>max:
        max=total
        result = x
print(result)

# 2번째 방법
n=int(input())
n_data=list(map(int,input().split()))
def digit_sum(x):
    sum=0
    for i in str(x):
        sum+=int(i)
    return sum

max=-2147000000
for x in n_data:
    total=digit_sum(x)
    if total>max:
        max=total
        result = x
print(result)
