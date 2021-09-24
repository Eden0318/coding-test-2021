import sys
input=sys.stdin.readline

def DFS(L):
    global cnt
    if L==m: #L==2  하나의 중복순열이 완성된 상태 즉 res=[] 다 들어있음
        for j in range(m):
            print(res[j],end='')
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            res[L]=i
            DFS(L+1)
        
if __name__=="__main__":
    n,m=map(int,input().split()) # 3 2
    cnt=0
    res=[0]*m
    DFS(0)
    print(cnt)