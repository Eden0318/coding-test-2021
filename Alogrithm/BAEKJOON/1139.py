n=int(input())
minutes=list(map(int,input().split()))
minutes.sort()
sum=0
for i in range(n):
    for j in range(i+1):
        sum+=minutes[j]

print(sum)
