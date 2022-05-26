N = int(input())
chaos = []
score = [1] *N
for _ in range(N):
    A, B  = map(int,input().split())
    chaos.append([A,B])
for y in range(len(chaos)):
    deso = 0
    for x in range(len(chaos)):
        if x == y:
            continue
        else:
            if chaos[y][0] < chaos[x][0] and chaos[y][1] < chaos[x][1]:
                score[y] += 1
                continue
            # elif chaos[y][0] > chaos[x][0] or chaos[y][1] > chaos[x][1]:
            #     continue

## 최대값에 1주고
## 그다음 최대값에 N- 1준만큼
## 그 다음 최대값에 N - 1준만큼 -2준만큼
print(*score)
