import sys
from collections import deque

def push_front(x):
    answer.appendleft(x)

def push_back(x):
    answer.append(x)

def pop_front():
    if answer:
        print(answer.popleft())
    else:
        print(-1)

def pop_back():
    if answer:
        print(answer.pop())
    else:
        print(-1)

def size():
    print(len(answer))

def empty():
    if answer:
        print(0)
    else:
        print(1)

def front():
    if answer:
        print(answer[0])
    else:
        print(-1)

def back():
    if answer:
        print(answer[-1])
    else:
        print(-1)

n=int(input())
answer = deque([]) #answer=deque()



for _ in range(int(n)):
    input_split = sys.stdin.readline().split()
    order = input_split[0] #push 4 입력

    if order=="push_front":
        push_front(input_split[1])

    elif order=="push_back":
        push_back(input_split[1])

    elif order=="pop_front":
        pop_front()

    elif order=="pop_back":
        pop_back()        
    
    elif order=="size":
        size()

    elif order=="empty":
        empty()

    elif order=="front":
        front()

    elif order=="back":
        back()        
    


