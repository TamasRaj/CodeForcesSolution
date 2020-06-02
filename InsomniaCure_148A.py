#Insomnia cure
#Problem Link : http://codeforces.com/problemset/problem/148/A

k , l , m , n , d = map(int , [input() , input() , input() , input() , input()])
num = [0] * (d + 1)
j = 0
for i in [k , l  , m , n]:
    for j in range(1 , 100001):
        try:
            num[i * j] = 1
        except:
            break
print(len([x for x in num if x == 1]))