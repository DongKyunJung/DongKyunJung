import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
x = []
y = []
for _ in range(6):
    direc, length = map(int, input().split())
    if direc == 1 or direc == 2:
        x.append(length)
    else:
        y.append(length)
answer = (max(x) * max(y) * N) - (min(x) * min(y) * N)
print(answer)