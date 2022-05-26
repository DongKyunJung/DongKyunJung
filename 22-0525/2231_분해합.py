n = int(input())

for k in range(1,n):
    answer = k
    for p in range(len(str(k))):
        answer += int(str(k)[p])
    if answer == n:
        print(k)
        break
else:
    print(0)