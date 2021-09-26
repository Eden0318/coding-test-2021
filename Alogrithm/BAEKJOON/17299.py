import sys
from collections import Counter

n=int(input())
a = list(map(int, sys.stdin.readline().split()))
stack=[]
answer=[-1]*n
cnt = Counter(a)

stack.append(0)
for i in range(1,n):
    while stack and cnt[a[stack[-1]]] < cnt[a[i]]:
        answer[stack.pop()]=a[i]
    stack.append(i)

print(*answer)    
