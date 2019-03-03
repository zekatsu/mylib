class RMQsegtree():
    def __init__(self, prog):
        self.size = len(prog) << 1
        self.tree = [10**9 for _ in range(self.size)]
        r = self.size
        l = r >> 1
        for i in range(l, r):
            self.tree[i] = prog[i-l]
        l >>= 1
        r >>= 1
        while l > 0:
            for i in range(l, r):
                self.tree[i] = min(self.tree[i << 1], self.tree[(i << 1) + 1])
            l >>= 1
            r >>= 1
    def mod(self, index, x):
        i = index + self.size
        self.tree[i] = x
        while i:
            self.tree[i] = min(self.tree[i << 1], self.tree[(i << 1) + 1])
    def rangemin(self, l, r):
        ret = 10**9
        gen = self.size
        while gen:
            if l & 1:
                ret = min(ret, self.tree[l + self.size])
            if r & 1:
                ret = min(ret, self.tree[r + self.size])
            l >>= 1
            r >>= 1
            gen >>= 1
        return ret