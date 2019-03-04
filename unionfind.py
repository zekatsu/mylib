class Unionfind():
    def __init__(self, progsize):
        self.table = [-1 for _ in range(progsize)]
        self.size = [1 for _ in range(progsize)]
    def find(self, x):
        while(self.table[x] >= 0):
            x = self.table[x]
        return x
    def union(self, x, y):
        xl = self.find(x)
        yl = self.find(y)
        if xl != yl:
            if self.table[xl] <= self.table[yl]:
                self.table[yl] = xl
                self.table[xl] -= 1
                self.size[xl] += self.size[yl]
            else:
                self.table[xl] = yl
                self.table[yl] -= 1
                self.size[yl] += self.size[xl]
