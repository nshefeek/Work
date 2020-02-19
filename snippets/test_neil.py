l = [2, 1, 5, 1, 3, 2]
k = 4
temp = 0
for i in range(0, len(l) - k + 1):
    print(l[i:i+k])
    result = sum(l[i:i+k])
    if result >= temp:
        temp = result

print(temp)
