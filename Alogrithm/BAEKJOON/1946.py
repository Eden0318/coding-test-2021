##**순위를 점수로 헷갈리지 말 것**
case=int(input())

for i in range(0,case):
    data=[]
    cnt=1
    n=int(input())

    for i in range(n):
        a,b = map(int,input().split())
        data.append([a,b])
    data.sort()
    largest=data[0][1]

    for i in range(1,n):
        if largest > data[i][1]:
            cnt+=1
            largest=data[i][1]
            
    print(cnt)