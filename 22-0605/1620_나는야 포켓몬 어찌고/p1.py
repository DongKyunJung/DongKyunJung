import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
pocketmon_number = {}
pocketmon_name = {}
num = 1
for _ in range(N):
    name = sys.stdin.readline().strip()
    pocketmon_number[name] = num
    pocketmon_name[num] = name
    num += 1

for _ in range(M):
    quest = sys.stdin.readline().strip()

    try:
        print(pocketmon_name[int(quest)])
    except:
        print(pocketmon_number[quest])
