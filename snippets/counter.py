def KFrequency (S, K):
    # Write your code here
    string = list(S)
    counter = {}
    
    for i in string:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    
    return (counter)

T = int(input())
for i in range(T):
    S = input()
    K = int(input())

    out_ = KFrequency(S, K)
    print (out_)
