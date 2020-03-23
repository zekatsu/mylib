N, W = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(N)]

maxw = 0
for _, y in A:
    maxw = max(maxw, y)

if maxw <= 1000:
    d = [0] *(W+1)
    for v, w in A:
        for j in reversed(range(W-w+1)):
            d[j+w] = max(d[j+w], d[j] + v)
    print(d[W])

else:
    d = {0: 0}
    for v, w in A:
        add = []
        for sumv, minw in d.items():
            if minw + w <= W:
                add.append((sumv + v, minw + w))
        for i, c in add:
            if i in d:
                d[i] = min(d[i], c)
            else:
                d[i] = c
    print(max(d.keys()))