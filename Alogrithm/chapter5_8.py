n=int(input()) #5
p=dict() #poem 
for i in range(n):
    word=input()
    p[word]=1

for i in range(n-1):
    word=input()
    p[word]=0

print(p)

for key,value in p.items():
    if value==1:
        print(key)
        break
    


