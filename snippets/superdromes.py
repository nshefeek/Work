cases = int(input())

nums = list(map(int, input().split()))


result = []

for i in nums:
    n = 1
    count = 0
    while n <= i:
        if str(bin(n))[2:] == str(bin(n))[2:][::-1]:
            count += 1 
        n += 1
        
    result.append(str(count))
    

    
print(' '.join(result))
