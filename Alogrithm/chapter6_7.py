import sys
def DFS(L,sum):
    global res
    if L>res: #cut-edge 시간 더 줄이기위함
        return
    if sum>m:
        return
    if sum==m:
        if L<res:
            res=L
    else:
        for i in range(n):
            DFS(L+1,sum+a[i])

if __name__=="__main__":
    n=int(input())
    a=list(map(int,input().split()))
    m=int(input())
    res=2147000000
    a.sort(reverse=True) # 5 2 1
    DFS(0,0) 
    print(res)