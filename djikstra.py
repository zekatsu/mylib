inf = 10 ** 9
s = set()
u = set()
dis = [inf] * n
for i in range(n):
    dis[i] = edge[0][i]
for _ in range(n):
    if u == set():
        break
    mindis = inf
    for i in u:
        if dis[i] < mindis:
            mindis = dis[i]
            m = i
    s.add(m)
    u.remove(m)
    for i in u:
        dis[i] = min(dis[i], dis[m] + edge[m][i])