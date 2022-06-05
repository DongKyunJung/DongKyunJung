import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
box = list(map(int, input().split()))
dictan = {}
for k in box:
    try:
        dictan[int(k)] += 1
    except:
        dictan[int(k)] = 1
M = int(input())
question = list(map(int, input().split()))
for k in question:
    try:
        print(dictan[k],end=' ')
    except:
        print('0',end=' ')

