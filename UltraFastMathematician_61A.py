#Ultra-Fast Mathematician
#Problem Link : http://codeforces.com/problemset/problem/61/A

n , m = input() , input()

for x , y in zip(n ,m):
    print("0" if x == y else "1", end='')