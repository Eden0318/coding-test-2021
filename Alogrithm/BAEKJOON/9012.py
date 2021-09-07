#내가 한 것 -> 망한 코드
#n=int(input()) #6
#stack=[] #( )
#for i in range(n):
#    k=list(input()) #( ( ) ) ( ) )
#    for j in range(len(k)):
#        if k[j]=="(":
#            stack.append(k[j])
#        else:
#            if k[j-1]=="(":
#                stack.pop()
#            else:
#                stack.append(k[j])
#
#    if len(stack)==0:
#        print("YES")
#    else:
#        print("NO")


a = int(input()) #6
for i in range(a):
    b = input() 
    s = list(b)
    sum = 0
    for i in s:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')  




#2번사례
#num = int(input())
#for i in range(num):
#  input_data = input() #( ( ) ) ( ) )
#  bracket = [] #
#
#  for j in input_data:
#    if j == "(":
#      bracket.append(j)
#    elif j == ")":
#      if len(bracket) != 0 and bracket[-1] == "(":
#        bracket.pop()
#      else:
#        bracket.append(")")
#        break
#
#  if len(bracket) == 0:
#    print("YES")
#  else:
#    print("NO")