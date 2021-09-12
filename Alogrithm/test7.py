n=int(input()) #8
a=list(map(int,input().split())) #5 3 4 0 2 1 1 0
seq=[0]*n #원수열
for i in range(n): #0~7
    for j in range(n): #0~7
        if a[i]==0 and seq[j]==0: #a[i]==0 자기 앞에 빈공간 확보했다는 뜻
            seq[j]=i+1
            break
        elif seq[j]==0:
            a[i]-=1

for x in seq:
    print(x,end=' ')
