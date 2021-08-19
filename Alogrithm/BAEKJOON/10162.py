#T=int(input()) #100
#A,B,C=300,60,10
#cnt=[]
#
#for i in A,B,C :
#    if i<=T:
#        cnt.append(T//i)
#        T=T%i
#    else:
#        cnt.append(0)

T = int(input())

if T % 10 != 0:
    print(-1)
else:
    A = B = C = 0
    A = T // 300
    B = (T % 300) // 60
    C = (T % 300) % 60 // 10
    print(A, B, C)