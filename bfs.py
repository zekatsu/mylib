def bfs(cur, searched):
    next = set()
    for x in cur:
        if x == end:
            return True
        if x not in searched:
            searched.add(x)
            for y in x.next:
                next.add(y)
    if next == set():
        return False
    else:
        return bfs(next, searched)