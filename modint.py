def extGCD(a, b):
    if b == 0:
        return a, 1, 0
    g, y, x = extGCD(b, a%b)
    y -= a//b * x
    return g, x, y

class Modint():
    def __init__(self, x):
        self.mod = 1000000007
        self.x = x % self.mod
    def __add__(self, other):
        return (self.x + other.x) % self.mod
    def __mul__(self, other):
        return (self.x * other.x) % self.mod
    def __sub__(self, other):
        return (self.x - other.x) % self.mod
    def __floordiv__(self, other):
        _, inv, _ = extGCD(other.x, self.mod)
        return (self.x * inv) % self.mod