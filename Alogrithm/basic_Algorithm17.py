n=9
a=[list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    if set(a[i])<n:
        print("No")
    for j in range(n):
        a[i][j]