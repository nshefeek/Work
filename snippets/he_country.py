t = int(input())

while t:
    n = int(input())
    A = list(map(int, input().split()))
    idx = 0
    count = 0
    while idx < len(A):
#        print(idx, A[idx], A[idx:idx+A[idx]])
        if (len(set(A[idx:idx+A[idx]])) == 1) & (A[idx] <= n):
            count += 1
        else:
            print('Invalid Data')
            break
        
        idx += A[idx]
    if idx == len(A):
        print(count)

    t -= 1

