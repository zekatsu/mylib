mod = 10 ** 9 + 7
def extGCD(a, b):
    if b == 0:
        return a, 1, 0
    g, y, x = extGCD(b, a%b)
    y -= a//b * x
    return g, x, y

def moddiv(a, b):
    _, inv, _ = extGCD(b, mod)
    return (a * inv) % mod

N = 10 ** 5 + 10
fact = [0] * (N)
fact[0] = 1
for i in range(1, N):
    fact[i] = (fact[i-1] * i) % mod

def comb(a, b):
    return moddiv(moddiv(fact[a], fact[a-b]), fact[b])