import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())