import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))
print(len(A ^ B))
