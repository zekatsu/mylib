inf = 10 ** 18
n, m = map(int, input().split())
d = [[inf for _ in range(n)] for _ in range(n)]

for i in range(n):
    d[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    d[a-1][b-1] = c
    d[b-1][a-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

for i in range(n):
    print(*d[i])