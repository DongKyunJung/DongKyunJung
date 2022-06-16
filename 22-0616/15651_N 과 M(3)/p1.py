import sys
input = sys.stdin.readline

def gogossing(box,N,M):
    if len(box) == M:
        print(*box)
        return
    for k in range(1,N+1):
        if box:
            if k >= box[-1]:
                box.append(k)
                gogossing(box,N,M)
                box.pop()
        else:
            box.append(k)
            gogossing(box, N, M)
            box.pop()
N, M = map(int, input().split())
box = []
gogossing(box,N,M)