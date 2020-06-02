#I_love_%username%
#Problem Link : http://codeforces.com/problemset/problem/155/A

n , l = int(input()) , list(map(int , input().split()))
low , high , amazing = l[0] , l[0] , 0
for i in l:
    if i > high:
        amazing += 1
        high = i
    elif i < low:
        amazing += 1
        low = i
print(amazing)