def pibo(arr,k):
    if k == n:
        return print(arr[k])
    
    arr.append(arr[-2]+arr[-1])
    pibo(arr,k+1)

arr = [0,1,1]
k = 2
n = int(input())

if n <= 2:
    print(arr[n])
else:
    pibo(arr,k)