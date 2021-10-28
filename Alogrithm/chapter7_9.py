from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]
board=[list(map(int,input().split())) for _ in range(7)]
dis=[[0]*7 for _ in range(7)]
Q=deque()
Q.append((0,0))
board[0][0]=1 #출발지점 Q에 넣으면서 1벽으로 만들어버림
while Q:
    tmp=Q.popleft()
    for i in range(4):
        x=tmp[0]+dx[i] #0
        y=tmp[1]+dy[i] #1
        if 0<=x<=6 and 0<=y<=6 and board[x][y]==0:
            board[x][y]=1 #다시 못가게 벽으로 만들어버림
            dis[x][y]=dis[tmp[0]][tmp[1]]+1
            Q.append(x,y) #(0,1)

if dis[6][6]==0:
    print(-1)
else:
    print(dis[6][6])