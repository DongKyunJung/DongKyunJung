import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
answer = []
bogi = {}
count = 0
for _ in range(N):
    bogi[input().strip()] = 0
print(bogi)
for _ in range(M):
    try:
        kk = input().strip()
        bogi[kk] += 1
        answer.append(kk)
        count += 1
    except:
        pass
print(count)
answer.sort()
for k in answer:
    print(k)

