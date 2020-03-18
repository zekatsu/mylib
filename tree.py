import sys
sys.setrecursionlimit(2*10**5)

n = int(input())
edge = [tuple(map(int, input().split())) for _ in range(n-1)]

connect = [set() for _ in range(n)]
for a, b in edge:
    connect[a-1].add(b-1)
    connect[b-1].add(a-1)

d = [0] * n

def dfs(v, dis, ng, d):
    d[v] = dis
    ng.add(v)
    for w in connect[v]:
        if w not in ng:
            dfs(w, dis+1, ng, d)

dfs(0, 0, set(), d)