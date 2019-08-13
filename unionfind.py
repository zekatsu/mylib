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
    
    def print(self):
        ret = {}
        for i in range(len(self.table)):
            p = self.find(i)
            if p not in ret:
                ret[p] = {i}
            else:
                ret[p].add(i)
        print(ret)

class Relativepos():
    def __init__(self, size):
        self.table = [[-1, 0] for _ in range(size)]

    def find(self, x):
        dis = 0
        while(self.table[x][0] >= 0):
            dis += self.table[x][1]
            x = self.table[x][0]
        return x, dis

    def union(self, x, y, d):
        xl, xd = self.find(x)
        yl, yd = self.find(y)
        if xl != yl:
            if self.table[xl][0] <= self.table[yl][0]:
                self.table[xl][0] += self.table[yl][0]
                self.table[yl] = [xl, xd + d - yd]
            else:
                self.table[yl][0] += self.table[xl][0]
                self.table[xl] = [yl, -xd - d + yd]
            return True
        else:
            return xd + d == yd

if __name__ == '__main__':
    n, q = map(int, input().split())
    query = [tuple(map(int, input().split())) for _ in range(q)]
    u = Unionfind(n)
    for p, a, b in query:
        if p == 0:
            u.union(a, b)
        if p == 1:
            print(['No', 'Yes'][u.same(a, b)])