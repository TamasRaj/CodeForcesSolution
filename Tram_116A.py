#Tram
#Problem Link : http://codeforces.com/problemset/problem/116/A

state = 0
cap = 0
n = int(input())

for _ in range(n):
    x , y = map(int , input().split())
    state += (y - x)
    if state > cap:
        cap = state
print(cap)