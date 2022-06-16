import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int,input().split())
box = [ y for y in range(1,N+1)]
cocoball = combinations(box, M)
for p in cocoball:
    print(*p)
