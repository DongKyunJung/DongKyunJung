import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

x_word = {}
y_word = {}

for _ in range(3):
    x, y = map(int, input().split())
    try:
        x_word[x] += 1

    except:
        x_word[x] = 1

    try:
        y_word[y] += 1
    except:
        y_word[y] = 1
for k in x_word:
    if x_word[k] == 1:
        print(k,end=' ')
for p in y_word:
    if y_word[p] == 1:
        print(p)