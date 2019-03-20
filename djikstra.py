s = set()
u = set()
dis = [10**9] * n
# init
for i in range(n):
    dis[i] = edge[i][s]
for _ in range(n):
    if u == set():
        break
    mindis = 10**9
    for i in u:
        if dis[i] < mindis:
            mindis = dis[i]
            a = i
    s.add(a)
    u.remove(a)
    for i in u:
        dis[i] = min(dis[i], dis[a] + edge[a][i])