##1
#n=int(input())
#meeting=[]
#
#for i in range(n):
#    s,e = map(int,input().split())
#    meeting.append((s,e))
#meeting.sort(key=lambda x : (x[1],x[0]))
#
#
#et=0
#cnt=0
#for s,e in meeting:
#    if s>=et:
#        et=e
#        cnt+=1
#print(cnt)

##2
#n=int(input())
#largest=0
#body=[]
#
#for i in range(n):
#    a,b = map(int,input().split())
#    body.append((a,b))
#body.sort(reverse=True)
    
#3
#n=int(input())
#h=list(map(int,input().split()))
#m=int(input())
#h.sort()
#for i in range(m):
#    h[0]+=1
#    h[n-1]-=1
#    h.sort()
#    
#print(h[n-1]-h[0])
    
#4

n,limit=map(int,input().split())
p=list(map(int,input().split()))
cnt=0
p.sort()
while p:
    if p[0]+p[-1]>limit:
        p.pop()
        cnt+=1
    else:
        p.pop(0)
        p.pop()
        cnt+=1   
print(cnt)



