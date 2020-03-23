n, m = map(int, input().split())
edge = [tuple(map(int, input().split())) for _ in range(m)]

inf = 10 ** 18
dis = [inf] * n
dis[0] = 0

for z in range(2*n+1):
    update = False
    for a, b, c in edge:
        a -= 1
        b -= 1
        if dis[a] != inf and dis[b] > dis[a] - c:
            dis[b] = dis[a] - c
            update = True
            if b == n - 1 and z >= n - 1:
                print('inf')
                exit()
print(-dis[n-1])