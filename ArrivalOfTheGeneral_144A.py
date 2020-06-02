#Arrival of the General
#Problem Link : http://codeforces.com/problemset/problem/144/A

n = int(input())
l = list(map(int , input().split()))
low = l[0]
high = l[0]
lowIndex = 0
highIndex = 0

for i , val in enumerate(l):
    if val <= low:
        lowIndex = i
        low = val
    if val > high:
        highIndex = i
        high = val
print(highIndex + n - lowIndex - 1 - (1 if lowIndex < highIndex else 0))