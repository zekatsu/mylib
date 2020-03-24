class Unionfind():
    def __init__(self, size):
        self.table = [-1 for _ in range(size)]

    def find(self, x):
        while(self.table[x] >= 0):
            x = self.table[x]
        return x

    def same(self, x, y):
        xp = self.find(x)
        yp = self.find(y)
        return xp == yp

    def union(self, x, y):
        xp = self.find(x)
        yp = self.find(y)
        if xp != yp:
            if self.table[xp] < self.table[yp]:
                self.table[xp] += self.table[yp]
                self.table[yp] = xp
            else:
                self.table[yp] += self.table[xp]
                self.table[xp] = yp

n, m = map(int, input().split())
edge = [tuple(map(int, input().split())) for _ in range(m)]
u = Unionfind(n)
ans = 0
for a, b, c in sorted(edge, key = lambda x: x[2]):
    if not u.same(a, b):
        ans += c
        u.union(a, b)
print(ans)