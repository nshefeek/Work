'''
# Sample code to perform I/O:

name = raw_input()          # Reading input from STDIN
print 'Hi, %s.' % name      # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import itertools

N = int(input())
digit = input().split()
K = int(input())

combinations = itertools.combinations(digit, K)

result = []
for item in combinations:
    num = int(''.join(item))
    print(item)
    if (num % 3 == 0) & (item[0] != '0'):
        result.append(num)

if result:
    print(max(result))
else:
    print(-1)
