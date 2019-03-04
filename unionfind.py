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
            if self.table[xp] <= self.table[yp]:
                self.table[yp] = xp
                self.table[xp] += self.table[yp]
            else:
                self.table[xp] = yp
                self.table[yp] += self.table[xp]