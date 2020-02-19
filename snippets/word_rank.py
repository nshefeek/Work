from itertools import permutations

def lexicographical_combos(word, rank):
    perm = sorted(''.join(chars) for chars in permutations(word))
    return(perm[rank-1])

n = int(input())
while n:
    word, rank = input().split()
    print(lexicographical_combos(word, int(rank)))
    n -= 1

