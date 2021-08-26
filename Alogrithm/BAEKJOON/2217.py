#n=int(input()) #2
#lope=[]
#
#for _ in range(n):
#    lope.append(int(input())) #10, 15
#lope.sort()
#
#
#weight = lope[0]*n 
#
#print(weight)


n=int(input()) #2
rope=[]
value=[]

for i in range(n):
    rope.append(int(input())) #10 15
rope.sort(reverse=True) #15 10

for num in range(n):
    value.append(rope[num]*(num+1)) #num번째 값을 최대 중량으로 할 때
print(max(value))


n = int(input()) # 로프의 개수

rope = [int(sys.stdin.readline()) for i in range(n)] # 각 로프가 버틸 수 있는 최대 중량 10 15

rope.sort() # 10 15

result=0

for i in range(len(rope)): #2
    if result < n * rope[i]:
        result = n * rope[i]
        n -= 1
    else:
        n -= 1

print(result)