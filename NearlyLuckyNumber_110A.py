#Nearly Lucky Number
#Problem Link : http://codeforces.com/problemset/problem/110/A

n = len([1 for ch in input() if ch == '4' or ch == '7'])
res = 'YES'
for ch in str(n):
    if ch != '4' and ch != '7':
        res = 'NO'
print(res)