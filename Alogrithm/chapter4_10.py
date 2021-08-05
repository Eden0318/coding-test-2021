n=int(input()) #8
a=list(map(int,input().split())) #5 3 4 0 1 1 0
seq=[0]*n #원수열
for i in range(1,n+1):
    for j in range(n): #0~7
        if a[i]==0 and seq[j]==0:
            seq[j]=i
            break
        elif seq[j]==0:
            a[i]-=1

for x in seq:
    print(x,end=' ')
