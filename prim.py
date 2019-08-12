from heapq import heappop, heappush
inf = 10 ** 18

n, m = map(int, input().split())
dis = [inf] * n
edge = [[] for _ in range(n)]
que = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edge[a-1].append((b-1, c))
    edge[b-1].append((a-1, c))

dis[0] = 0
heappush(que, (0, 0))
unsearched = [True] * n
ans = 0

while que != []:
    # print(*dis)
    # print(que)
    d, v = heappop(que)
    if unsearched[v]:
        unsearched[v] = False
        ans += d
        for to, cost in edge[v]:
            if dis[to] > cost:
                dis[to] = cost
                heappush(que, (dis[to], to))

print(ans)