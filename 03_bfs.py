from collections import deque

g = {0:[1,2], 1:[3], 2:[3], 3:[]}
q, seen, order = deque([0]), {0}, []
while q:
    v = q.popleft(); order.append(v)
    for u in g[v]:
        if u not in seen: seen.add(u); q.append(u)

print(order)
