import heapq as hq
inf = 10 ** 18

n, m = map(int, input().split())
dis = [inf] * n
edge = [[] for _ in range(n)]
que = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edge[a-1].append((b-1, c))

dis[0] = 0
hq.heappush(que, (0, 0))

while que != []:
    # print(*dis)
    # print(que)
    d, v = hq.heappop(que)
    if d == dis[v]:
        for to, cost in edge[v]:
            if dis[to] > d + cost:
                dis[to] = d + cost
                hq.heappush(que, (dis[to], to))