from collections import deque

#1
n=int(input())
for i in range(n):
    word=input().upper()
    if word == word[::-1]:
        print("YES")
    else:
        print("NO")
        
        
#1-1
n=int(input())
for i in range(n):
    s=input().upper()
    size=len(s)

for j in range(size//2):
    if s[j]!=s[-1-j]:
        print("NO")
        
    else:
        print("YES")