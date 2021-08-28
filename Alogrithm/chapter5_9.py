a=input() #AbaAeCe 2 1 1 2 1  
b=input() #baeeACA 1 1 2 2 1  
str1=dict()
str2=dict()

#print(str1)

for x in a:
    str1[x]=str1.get(x,0)+1

for x in b:
    str2[x]=str2.get(x,0)+1

#print(str1)
#print(str2)


for i in str1.keys():
    if i in str2.keys():
        if str1[i]!=str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")    