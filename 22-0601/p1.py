import sys
sys.stdin = open('input.txt')

N = map(int, input())
my_card = sorted(map(int, input().split()))
M = map(int, input())
num_card = list(map(int, input().split()))
answer = []

def binary(k, my_card, start, end):
    mid = (start+end) // 2
    if start > end:
        answer.append(str(0))
    elif k == my_card[mid]:
        answer.append(str(1))
    elif k > my_card[mid]:
        binary(k, my_card, mid+1, end)
    else:
        binary(k, my_card, start, mid-1)

for k in num_card:
    start = 0
    end = len(my_card)-1
    binary(k, my_card, start, end)

print(' '.join(answer))

