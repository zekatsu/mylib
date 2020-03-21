x, y = map(int, input().split())

l = [[0 for _ in range(20)] for _ in range(20)]

def next(x, y):
    ret = []
    for i in range(1, x // 2 + 1):
        ret.append((x - i*2, y + i))
    for i in range(1, y // 2 + 1):
        ret.append((x + i, y - i*2))
    return ret

def win(x, y):
    if (x, y) in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        return False
    else:
        for i, j in next(x, y):
            if not win(i, j):
                return True
        return False

N = 10
test = ['' for _ in range(N)]
for i in range(N):
    for j in range(N):
        if win(i, j):
            test[i] += 'W'
        else:
            test[i] += 'L'

for x in test:
    print(x)