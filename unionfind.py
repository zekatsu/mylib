class Unionfind():
    def __init__(self, size):
        self.table = [-1 for _ in range(size)]

    def find(self, x):
        while(self.table[x] >= 0):
            x = self.table[x]
        return x

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