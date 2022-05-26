N = int(input())
chaos = []
for _ in range(N):
    A, B  = map(int,input().split())
    chaos.append([A,B])
chaos.sort(key=lambda x : -x[1])
print(chaos)
