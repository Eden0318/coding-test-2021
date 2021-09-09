import sys
def push(x):
    QUEUE.append(x)

def pop():
     return QUEUE.pop(0) if QUEUE else -1

def size():
    return len(QUEUE)

def empty():
    if len(QUEUE)==0:
        print(1)
    else:
        print(0)

def front():
    print(QUEUE[0])

def back():
    print(QUEUE[-1])

QUEUE=[]

n=int(input())
for _ in range(n):
    input_split = sys.stdin.readline().split() #push 1
    order = input_split[0]

    if order=="push":
        push(input_split[1])

    elif order=="pop":
        print(pop())

    elif order=="size":
        print(size())
    
    elif order=="empty":
        if len(QUEUE)==0:
            print(1)
        else:
            print(0)
    elif order=="front":
        if len(QUEUE)!=0:
            print(QUEUE[0])
        else:
            print(-1)

    elif order=="back":
        if len(QUEUE)!=0:
            print(QUEUE[-1])
        else:
            print(-1)



        



    