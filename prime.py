MAX_PRIME = 10 ** 6
is_prime = [1] * MAX_PRIME
primes = []
is_prime[0] = 0
is_prime[1] = 0
for i in range(MAX_PRIME):
    if is_prime[i]:
        primes.append(i)
        for j in range(2, ((MAX_PRIME-1)//i) + 1):
            is_prime[i*j] = 0

def factorization(n):
    factor = {}
    for p in primes:
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

n = int(input())
f = factorization(n)
k = list(f.keys())
def dfs(num, i):
    if i == len(k):
        # 約数に対して何か行う
    else:
        p = k[i]
        for j in range(f[p]+1):
            ret += dfs(num * p ** j, i+1)