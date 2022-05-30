import sys
sys.stdin = open('input.txt')

N = int(input())

t = 665
k = 0
while True:
    t += 1
    if '666' in str(t):
        k += 1
    if k == N:
        print(t)
        break

