INF = 2 * 10**9
class RQ():
    def __init__(self, prog):
        k = 1
        while k < len(prog):
            k <<= 1
        prog += [INF] * (k - len(prog))
        self.size = k
        r = self.size
        l = r >> 1
        self.tree = [prog[i] for i in range(self.size)] * 2
        self.tree[0] = INF
        while l:
            for i in range(l, r):
                if self.tree[i << 1] == self.tree[(i << 1) + 1]:
                    self.tree[i] = self.tree[i << 1]
                else:
                    self.tree[i] = INF
            l >>= 1
            r >>= 1
    def mod(self, l, r):
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
    def print(self):
        print(*self.tree)
        k = 1
        size = 2
        for n in self.tree[1:]:
            k += 1
            print(n, end = ' ')
            if k == size:
                print()
                size *= 2

if __name__ == '__main__':
    a = [1, 9, 8, 8, 8, 8, 8, 2, 2, 2, 3, 4]
    q = RQ(a)
    q.print()