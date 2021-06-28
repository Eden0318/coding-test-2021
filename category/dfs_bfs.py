#deque 라이브러리
#from collections import deque
#
#queue = deque()
#
#queue.append(5)
#queue.append(2)
#queue.append(3)
#queue.append(7)
#queue.popleft()
#queue.append(1)
#queue.append(4)
#queue.popleft()
#
#print(queue)
#queue.reverse()
#print(queue)

#p.149

n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))
#print(graph)

def dfs(x,y):
    if x<=1 or x>n or y<=-1 or y>=m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
