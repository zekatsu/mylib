import heapq as hq
inf = 10 ** 9

n, m = map(int, input().split())
dis = [inf] * n
edge = [[] for _ in range(n)]
searched = [False] * n
que = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edge[a].append((b, c))

dis[0] = 0
hq.heappush(que, (0, 0))

while que != []:
    print(*dis)
    print(que)
    d, v = hq.heappop(que)
    if not searched[v]:
        searched[v] = True
        for to, cost in edge[v]:
            if searched[to]:
                continue
            if dis[to] > d + cost:
                dis[to] = d + cost
                hq.heappush(que, (dis[to], to))