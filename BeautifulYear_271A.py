#Beautiful year
#Problem Link : http://codeforces.com/problemset/problem/271/A

def isUnique(n):
    l = list(str(n))
    if len(set(l)) == len(l):
        return True
    return False

n = int(input())
n += 1
while True:
    if isUnique(n):
        print(n)
        break
    n += 1
