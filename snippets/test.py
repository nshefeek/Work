# # [1, 3, 4, -5, 6, -2, -5]

# l = [1, 3, 4, -5, 6, -2, -5]

# result = sum([i for i in l if i >= 0])

# print(result)

# '-345'

# s = '-345'

# print('-', s[len(s) - 1:0:-1], sep='')
# import itertools

# l = [6, 7, 5, 6, 4, 3, 2, 8, 1]

# size = 3

# combinations = itertools.combinations(l, size)
# result = {}

# for item in combinations:
#     result[item] = sum(item)

# max_sum = max(result.values())

# #print(max_sum)

# for i in result.keys():
# 	if result[i] == max_sum:
# 		print(i, max_sum)

# s = 'hello world ll'
# n = 'q'

# length = len(s)
# window = len(n)

# count = 0
# for i in range(length - 1):
#     if n == s[i:i + 2]:
#         count += 1
# help(n.count)

# print(s.find(n))

