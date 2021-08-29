n,limit=map(int,input().split())
p=list(map(int,input().split()))
cnt=0
p.sort()
while p:
    if p[0]+p[-1]>limit:
        p.pop()
        cnt+=1
    else:
        p.pop(0)
        p.pop()
        cnt+=1   
print(cnt)