from collections import deque
n,k=map(int,input().split())

dq=list(range(1,n+1)) #1,2,3,4,5,6,7,8
dq=deque(dq)

while dq:
    for _ in range(len(k-1)):
        cur=dq.popleft()
        dq.append(cur)
    dq.popleft()

        

