import sys
from collections import deque
MAX=100000
ch=[0]*(MAX+1)
dis=[0]*(MAX+1)
n,m=map(int,input().split()) # 5, 14
ch[n]=1 # 맨 처음 시작 처리
dis[n]=0
dQ=deque()
dQ.append(n)

while dQ:
    now=dQ.popleft()
    if now==m: #now==14
        break
    for next in(now-1,now+1,now+5): #3 5 9
        if 0<next<=MAX:
            if ch[next]==0:
                dQ.append(next)
                ch[next]=1
                dis[next]=dis[now]+1
print(dis[m])
