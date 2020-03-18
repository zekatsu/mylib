h, w = map(int, input().split())
start = tuple(map(int, input().split()))
goal = tuple(map(int, input().split()))
f = [input() for _ in range(h)]

def next(pos):
    x, y = pos
    ret = []
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        ret.append((x + dx, y + dy))
    return ret

s = {start}
ng = set()
ans = 0
while True:
    t = set()
    for p in s:
        if p == goal:
            print(ans)
            exit()
        ng.add(p)
        for x, y in next(p):
            if (x, y) not in ng and f[x-1][y-1] != '#':
                t.add((x, y))
    s = t
    ans += 1