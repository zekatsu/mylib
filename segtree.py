class RMQsegtree():
    def __init__(self, prog):
        k = 1
        while k < len(prog):
            k <<= 1
        prog += [2 * 10**9] * (k - len(prog))
        self.size = k
        r = self.size
        l = r >> 1
        self.tree = [prog[i] for i in range(self.size)] * 2
        while l:
            for i in range(l, r):
                self.tree[i] = min(self.tree[i << 1], self.tree[(i << 1) + 1])
            l >>= 1
            r >>= 1
    def mod(self, index, x):
        i = index + self.size
        self.tree[i] = x
        while i:
            self.tree[i] = min(self.tree[i << 1], self.tree[(i << 1) + 1])
    def minimum(self, l, r):
        ret = 10**9
        l += self.size
        r += self.size
        while r - l > 0:
            if l & 1:
                ret = min(ret, self.tree[l])
                l += 1
            if r & 1:
                ret = min(ret, self.tree[r-1])
            l >>= 1
            r >>= 1
        return ret
import random
a = [random.randrange(100) for _ in range(1000)]
n = len(a)
sta = RMQsegtree(a)
for l in range(n):
    for r in range(l+1, n):
        if min(a[l:r]) != sta.minimum(l,r):
            print('range({}, {})'.format(l,r))
            print(min(a[l:r]), sta.minimum(l,r))