import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

x, y, w, h = map(int, input().split())
print(min(abs(0-x),abs(w-x),abs(0-y),abs(h-y)))