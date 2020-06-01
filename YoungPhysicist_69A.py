#Young Physicist
n = input()
I , J , K = 0 , 0 , 0
for _ in range(int(n)):
    i , j , k = map(int , input().split())
    I += i
    J += j
    K += k
 
print("YES" if I == 0 and J == 0 and K == 0 else "NO")