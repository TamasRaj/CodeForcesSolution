#Petya and Strings
#Problem Link : http://codeforces.com/problemset/problem/112/A

s1 , s2 = input().upper() , input().upper()
if s1 == s2:
    print(0)
elif s1 < s2 :
    print(-1)
else:
    print(1)
