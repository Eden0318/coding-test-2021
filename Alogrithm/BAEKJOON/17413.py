import sys
from collections import deque

q=deque() #태그는 뒤집을게 아니기 때문에 데크 사용
stack=[] #문자는 뒤집어야 하기 때문에 후입선출 스택 사용
result='' #최종결과물 출력
state=True #태그안의 단어인지 일반 단어인지 구분하기 위한 flag
str=list(sys.stdin.readline().strip())#banana <kiwi> apple

for i in str:
    if i=="<":
        while stack:
            result+=stack.pop()
        q.append(i)
        state=False

    elif i==">":
        q.append(i)
        state=True
        while q:
            result+=q.popleft()    
        
    elif i==" ": #태그안에서 공백인지 밖에서 공백인지
        if state:
            while stack:
                result+=stack.pop()
            result+=" "
        else:
            q.append(i)
            while q:
                result+=q.popleft()

    else:
        if state:
            stack.append(i)
        else:
            q.append(i)

while stack:
    result+=stack.pop()

print(result)
    














#n=list("apple")
#n.reverse()
#print(''.join((list(n))), end=" ")

