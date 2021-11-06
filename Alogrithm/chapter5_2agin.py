s=input() 
cnt=0
stack=[]

for i in range(len(s)): #18
    if s[i]=="(":
        stack.append(s[i])
    else:
        if s[i-1]=="(":
            stack.pop()
            cnt+=len(stack)
        else:
            stack.pop()
            cnt+=1    
        
print(cnt)




