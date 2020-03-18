d = [0] * (10 ** 6 + 2)
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    d[a] += 1
    d[b+1] -= 1
c = 0
ans = 0
for x in d:
    c += x
    ans = max(ans, c)
print(ans)