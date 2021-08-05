class Primes:

    def __init__(self, MAX_PRIME):
        self.is_prime = [1] * MAX_PRIME
        self.primes = []
        self.is_prime[0] = 0
        self.is_prime[1] = 0
        for i in range(MAX_PRIME):
            if self.is_prime[i]:
                self.primes.append(i)
                for j in range(2, ((MAX_PRIME-1)//i) + 1):
                    self.is_prime[i*j] = 0

    def factorization(self, n):
        factor = {}
        for p in self.primes:
            if p ** 2 > n:
                break
            while n % p == 0:
                n //= p
                if p not in factor:
                    factor[p] = 1
                else:
                    factor[p] += 1
        if n > 1:
            factor[n] = 1
        return factor

    def divisor(self, n):
        div = {n}
        fact = self.factorization(n)
        for p in fact.keys():
            new_div = div.copy()
            for i in range(1, fact[p] + 1):
                for d in div:
                    assert((d % p ** i) == 0)
                    new_div.add(d // p ** i)
            div = new_div
        return sorted(div)


if __name__ == '__main__':
    n = int(input())
    p = Primes(10 ** 6)
    print(p.factorization(n))
    print(p.divisor(n))