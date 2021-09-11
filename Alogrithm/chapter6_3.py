def DFS(v):
    if v==n+1: #종료지점 v==4
        for i in range(1,n+1):
            if ch[i]==1:
                print(i,end='')
        print()
    else:
        ch[v]=1
        DFS(v+1)
        ch[v]=0
        DFS(v+1)

if __name__=="__main__":
    n=int(input()) #3
    ch=[0]*(n+1)
    DFS(1)