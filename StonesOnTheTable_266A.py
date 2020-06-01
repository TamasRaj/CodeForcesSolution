#Stones on the Table
#Problem Link : http://codeforces.com/problemset/problem/266/A

_ , s = input() , input()
count = 0
last = s[0]

for ch in s[1:]:
    if last == ch:
        count += 1
    last = ch
print(count)

