import heapq as hq

a=[] #힙자료구조
while True:
    n=int(input()) 
    if n==-1: #-1이 입력되면 종료
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a,n)