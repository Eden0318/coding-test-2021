#Q1
n = int(input())
x,y=1,1
plans=input().split()

dx=[0,0,-1,1]
dy=[-1,1,-0,0]
move_types=["L","R","U","D"]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x+dx[i]
            ny = y+dy[i]
            
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    
    x,y=nx,ny
    
print(x,y)

#Q2

h=int(input())

count=0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1

print(count)

dot = list(input())


#Q3
input_data = input()
row=int(input_data[1])
column = int(ord(input_data[0]))-int(ord("a"))+1
result=0

dx = [-1,1,2,2,1,-1,-2,-2]
dy = [2,2,1,-1,-2,-2,-1,1]
for i in range(len(dx)):
    nx = row+dx[i]
    ny = column+dy[i]
    if nx<1 or ny<1 or nx>8 or ny>8:
        continue
    result+=1

print(result)
