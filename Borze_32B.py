#Borze
#Problem Link : http://codeforces.com/problemset/problem/32/B

code = input()
letter = []
for c in code:
    letter.append(c)
    s = ''.join(letter)
    if s == '.':
        print(0 , end='')
        letter = []
    elif s == '-.':
        print(1 , end='')
        letter = []
    elif s == '--':
        print(2 , end='')
        letter = []