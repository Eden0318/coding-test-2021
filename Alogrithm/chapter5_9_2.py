a=input()
b=input()
str1=[0]*52 #알파벳 대문자+소문자 개수
str2=[0]*52

for x in a:
    if x.isupper():
        str1[ord(x)-65]+=1 #카운팅 대문자 0~25
    else:
        str1[ord(x)-71]+=1# 소문자는 26부터 나오게

for x in b:
    if x.isupper():
        str2[ord(x)-65]+=1 #카운팅 대문자 0~25
    else:
        str2[ord(x)-71]+=1# 소문자는 26부터

for i in range(52):
    if str1[i]!=str2[i]:
        print("NO")
        break
else:
    print("YES")        