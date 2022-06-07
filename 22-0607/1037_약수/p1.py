import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
box = list(map(int, input().split()))
print(max(box) * min(box))