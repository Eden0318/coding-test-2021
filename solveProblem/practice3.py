n,m=map(int,input().split())
n=list(str(n))

for i in range(len(n)):
    if n[i]<n[i+1]:
        n.pop(i)
        m-=1
        if m==0:
            break
print(n)


