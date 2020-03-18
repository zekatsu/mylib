n = int(input())
a = [int(input()) for _ in range(n)]
d = {}
for x in a:
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1

key = sorted(list(d.keys()))
order = {}
for i, c in enumerate(key):
    order[c] = i

b = list(map(lambda x: order[x], a))