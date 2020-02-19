total = 0
lines = []
with open('pe1.txt','r') as f:
    for i in range(7):
        try:
            num = int(f.readline().rstrip()[0])
            total += num
        except:
            print('Error')
            continue
    print(total)
