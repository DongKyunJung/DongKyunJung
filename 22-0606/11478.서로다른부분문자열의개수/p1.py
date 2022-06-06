import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

word = input()
answer = set()
for i in range(len(word)):
    for k in range(i, len(word)):
        answer.add(word[i:k+1])
print(answer)
print(len(answer))
