from cmath import inf
import sys
sys.stdin = open('input.txt')

def chess(y, x):
    global result

    ## 시작이 W일경우
    score = 0
    if chess_board[y][x] != 'W':
        score += 1

    for ny in range(8):
        for nx in range(8):
            if ny + nx == 0 or (ny + nx) % 2 == 0:
                if chess_board[y + ny][x + nx] != 'W':
                    score += 1
            else:
                if chess_board[y + ny][x + nx] != 'B':
                    score += 1
    if score < result:
        result = score

    ## 시작이 B일경우
    score = 0
    if chess_board[y][x] != 'B':
        score += 1

    for ny in range(8):
        for nx in range(8):
            if ny + nx == 0 or (ny + nx) % 2 == 0:
                if chess_board[y + ny][x + nx] != 'B':
                    score += 1
            else:
                if chess_board[y + ny][x + nx] != 'W':
                    score += 1
    if score < result:
        result = score


Y, X = map(int, input().split())
chess_board = []
result = float("inf")
for _ in range(Y):
    chess_board.append(list(map(str, input())))

for y in range(Y - 8 + 1):
    for x in range(X - 8 + 1):
        chess(y, x)
print(result)