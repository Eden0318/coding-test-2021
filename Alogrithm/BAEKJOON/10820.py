#리스트로 쪼개서 인덱스로 받아와서 문제를 풀려고 한게 문제였음

import sys
while True:
    line = sys.stdin.readline().rstrip("\n") #오른쪽에서 엔터치는 부분의 공백만 지워줌
    l,u,d,s=0,0,0,0

    if not line:
        break
    for i in line:
        if i.islower():
            l+=1
        elif i.isupper():
            u+=1
        elif i.isdigit():
            d+=1
        elif i.isspace():
            s+=1

    print(l,u,d,s)    
