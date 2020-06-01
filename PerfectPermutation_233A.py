#Perfect Permutation
#Problem Link : http://codeforces.com/problemset/problem/233/A

n = int(input())
l = []
if n % 2 == 0:
    for i in range(1 , n + 1 , 2):
        l.append(str(i + 1))
        l.append(str(i))
    print(" ".join(l))
else:
    print(-1)