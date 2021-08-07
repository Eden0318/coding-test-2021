#3
n,m = map(int,input().split())
Music = list(map(int,input().split()))
lt=1
rt=max(Music)

def Count(capacity):
    cnt=1
    sum=0
    for i in  Music:
        if sum+i>capacity:
            cnt+=1
            sum=i
        else:
            sum+=i
    return cnt


while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid)<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1

print(res)

#4


