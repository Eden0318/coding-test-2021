import sys


def push(X):
    stack.append(X)

def pop():
    if stack:
        return stack.pop()
    else:
        return -1

def size():
    return len(stack)


def empty():
    if stack:
        return 0
    else:
        return 1

def top():
    if stack:
        return stack[-1] if stack else -1
        


stack=[]
n=int(input())

for _ in range(n):
    str=sys.stdin.readline().strip()
    order=str[0]
    
    if order=="push":
        push(str[1])

    elif order=="pop":
        print(pop())

    elif order=="size":
        print(size())

    elif order=="empty":
        print(empty())
        
    elif order=="top":
        print(top())






