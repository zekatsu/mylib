n = int(input())
counter = {}
for _ in range(n):
    s = input()
    if s not in counter:
        counter[s] = 1
    else:
        counter[s] += 1
m = 0
ans = ''
for i, c in counter.items():
    if c > m:
        m = c
        ans = i
print(ans)