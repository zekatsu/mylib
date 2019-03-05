MAX_PRIME = 10**9
is_prime = [1] * MAX_PRIME
primes = []
is_prime[0] = 0
is_prime[1] = 0
for i in range(MAX_PRIME):
    if is_prime[i]:
        primes.append(i)
        for j in range(2, ((MAX_PRIME-1)//i) + 1):
            is_prime[i*j] = 0