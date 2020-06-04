#Team
#Problem Link : http://codeforces.com/problemset/problem/231/A

n = int(input())
print(len([i for i in range(n) if sum(map(int , input().split())) > 1]))