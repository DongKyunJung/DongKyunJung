import sys
input = sys.stdin.readline
def gogossing(box,y,x):



N = int(input())
answer = 0
box = [[0 for _ in range(N)] for _ in range(N)]
for y in range(N):
    for x in range(N):
        box[y][x] = 1
        gogossing(box,y,x)
        box[y][x] = 0
print(box)