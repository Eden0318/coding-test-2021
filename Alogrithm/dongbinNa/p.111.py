n=int(input())
dx=[-1,0,1,0]
dy=[0,1,0,-1]
x,y=1,1
move_plan=input().split()
move_type=["U","R","D","L"]

for i in move_plan:
    for j in range(len(move_type)):
        if i==move_type[j]:
            xx=x+dx[j]
            yy=y+dy[j]


    if xx<1 or yy<1 or xx>n or yy>n:
        continue
    x=xx
    y=yy

print(x,y)