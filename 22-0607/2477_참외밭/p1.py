import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
dir = []
leng = []
max_x = 0
max_y = 0
box_x = 0
box_y = 0
for _ in range(6):
    direc, length = map(int, input().split())
    dir.append(direc)
    leng.append(length)
for k in range(6):
    if dir.count(dir[k]) == 1:
        if dir[k] == 1 or dir[k] == 2:
            max_x = leng[k]
        else:
            max_y = leng[k]
print(leng)
print(dir)
print(max_x)
print(max_y)
for p in range(6):
    if dir[p] == 1 or dir[p] == 2:
        if not (leng[int(p+1) % 6] == max_y or leng[int(p-1)] == max_y):
            box_x = leng[p]

    else:
        if not (leng[int(p+1) % 6] == max_x or leng[int(p-1)] == max_x):
            box_y = leng[p]


answer = (max_x * max_y) - (box_x * box_y)
print(answer * N)

