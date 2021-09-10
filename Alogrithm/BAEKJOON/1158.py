from collections import deque

n,k=map(int,input().split())
dq=deque(list(range(1,n+1))) 
answer=[] 

while dq:
    for _ in range(k):
        x=dq.popleft()
        dq.append(x) 
    answer.append(dq.pop()) 
print("<"+", ".join(map(str,answer))+">")       


