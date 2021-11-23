import sys

def DFS(L,sum): 
    if sum>total//2:
        return
    if L==n: #L==6
        if sum==(total-sum): #total-sum은 내가 만들지 않은 반대쪽 부분집합
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1,sum+a[L])
        DFS(L+1,sum)

if __name__=="__main__":
    n=int(input())#6
    a=list(map(int,input().split()))
    total=sum(a) #32
    DFS(0,0)
    print("NO")