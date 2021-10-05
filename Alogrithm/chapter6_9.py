#조합문제
import sys
def DFS(L):
    global cnt
    if L==m:#m==2
        for j in range(L):
            print(res[j], end=" ")
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1)
                ch[i]=0


if __name__=="__main__":
    n,m=map(int,input().split()) # n=4, m=2
    res=[0]*m
    ch=[0]*(n+1)
    cnt=0
    DFS(0)
    print(cnt)