#v는 노드값, 전위순회
def DFS(v):
    if v>7:
        return #종료
    else:
        print(v,end='')
        DFS(v*2, end="") #부모곱하기 2 = 왼쪽노드
        DFS(v*2+1) #오른쪽노드

#v는 노드값, 중위순회
def DFS(v):
    if v>7:
        return #종료
    else:
        DFS(v*2, end="") #부모곱하기 2 = 왼쪽노드
        print(v,end='')
        DFS(v*2+1) #오른쪽노드


#v는 노드값, 후위순회
def DFS(v):
    if v>7:
        return #종료
    else:
        DFS(v*2, end="") #부모곱하기 2 = 왼쪽노드
        DFS(v*2+1) #오른쪽노드
        print(v,end='')


if __name__=="__main__":
    DFS(1)