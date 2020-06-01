#Word
#Problem Link : http://codeforces.com/problemset/problem/59/A

word = input()
n = len(word)
uCount = 0
for letter in word:
    if letter.isupper():
        uCount += 1
print(word.upper() if uCount > n // 2 else word.lower())