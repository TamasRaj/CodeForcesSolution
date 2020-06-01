#Beautiful Matrix
#Problem Link : http://codeforces.com/contest/263/problem/A
l = list()
m , n = -1 , -1
for m in range(5):
    i = input().split()
    try:
        n = i.index('1')
        if n != -1:
            print(abs(2 - m) + abs(2 - n))
    except:
        pass