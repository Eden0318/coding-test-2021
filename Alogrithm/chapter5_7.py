from collections import deque

need=input() #cba 
n=int(input()) #플랜갯수
for i in range(n):
    plan=input() #플랜 CBDAGE ECBA
    dq=deque(need) #cba
    for x in plan: 
        if x in dq: 
            if x != dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq)==0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))



