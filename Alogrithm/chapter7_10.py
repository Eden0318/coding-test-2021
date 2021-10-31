dx=[-1,0,1,0]
dy=[0,1,0,-1]

def DFS(x,y):
    global cnt
    if x==6 and y==6:
        cnt+=1
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]



if __name__=="__main__":
    board=[list(map(int,input().split()))]
    cnt=0
    board[0][0]=1
    DFS(0,0)



