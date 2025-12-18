g = {0:[1,2], 1:[3], 2:[3], 3:[]}
seen, order = set(), []

def dfs(v):
    seen.add(v); order.append(v)
    for u in g[v]:
        if u not in seen: dfs(u)

dfs(0)
print(order)
