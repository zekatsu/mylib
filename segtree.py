class RMQ():
    def __init__(self, array):
        k = 1
        while k < len(array):
            k <<= 1
        self.halflen = k
        self.tree = [0] * k + array + [10 ** 18] * (k - len(array))
        for i in reversed(range(k)):
            self.tree[i] = min(self.tree[i << 1], self.tree[(i << 1) | 1])

    def update(self, i, value):
        i |= self.halflen
        self.tree[i] = value
        i >>= 1
        while i:
            self.tree[i] = min(self.tree[i << 1], self.tree[(i << 1) | 1])
            i >>= 1

    def query_(self, i, left, right, l, r):
        if (left, right) == (l, r):
            return self.tree[i]
        ret = 10 ** 18
        m = (l + r) >> 1
        if left <  m:
            ret = min(ret, self.query_(i << 1, left, min(m, right), l, m))
        if right > m:
            ret = min(ret, self.query_((i << 1) | 1, max(left, m), right, m, r))
        return ret

    def query(self, left, right):
        return self.query_(1, left, right, 0, self.halflen)