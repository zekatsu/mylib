N = int(input())
S = input()

counter = {}
for x in S:
    if x in counter:
        counter[x] += 1
    else:
        counter[x] = 1