#두가지 DFS 차이점 이해하기

#321로 출력됨
# def DFS(x):
#    if x>0:
#        print(x, end='')
#        DFS(x-1)
        

#스택으로 인해 123으로 출력됨
def DFS(x):
    if x>0:
        DFS(x-1)
        print(x, end='')

if __name__ == "__main__":
    n=int(input())
    DFS(n)