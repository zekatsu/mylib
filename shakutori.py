n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

if 0 in a:
    print(n)
    exit()

a.append(0)
l, r = 0, 0
m = 1
ans = 0
while r < n+1:
    if m > k:
        if l < r:
            m //= a[l]
            l += 1
        else:
            m *= a[r]
            r += 1
    else:
        ans = max(ans, r - l)
        m *= a[r]
        r += 1

print(ans)