n=int(input())
p=dict()
for i in range(n):
    word=input()
    p[word]=1

for i in range(n-1):
    word=input()
    p[word]=0

for key, val in p.items():
    if val!=0:
        print("answer is"+key)
        break