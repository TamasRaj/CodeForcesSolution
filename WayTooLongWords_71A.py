#Way Too Long Words
#Problem Link : http://codeforces.com/problemset/problem/71/A

n = int(input())
for _ in range(n):
    s = input()
    print(''.join([s[0],str(len(s) - 2) , s[-1]]) if len(s) > 10 else s)