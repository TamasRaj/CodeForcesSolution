#Soft Drinking
#Problem Link : http://codeforces.com/problemset/problem/151/A

n, k, l, c, d, p, nl, np = map(int , input().split())
tv = k * l
ls = c * d
perToastV = n * nl
perToastS = n * np

print(min(tv // perToastV , ls // n , p // perToastS))
