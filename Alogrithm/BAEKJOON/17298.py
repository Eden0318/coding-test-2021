import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split())) # 3 5 2 7
answer = [-1] * n #[-1,-1,-1,-1]
stack = []

stack.append(0)
for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

print(*answer)
