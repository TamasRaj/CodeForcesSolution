#Queue at the School
#Problem Link : http://codeforces.com/problemset/problem/266/B

n , m = map(int , input().split())
l = list(input())
for _ in range(m):
    i = 1
    while i < n:
        if l[i] == 'G' and l[i-1] == 'B':
            l[i] , l[i - 1] = l[i - 1] , l[i]
            i += 1
        i += 1
print(''.join(l))