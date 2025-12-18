p = list(range(6))

def find(x):
    while p[x] != x:
        p[x] = p[p[x]]
        x = p[x]
    return x

def union(a,b):
    ra, rb = find(a), find(b)
    if ra != rb: p[rb] = ra

union(1,2); union(2,3); union(4,5)
print(find(3), find(5), [find(i) for i in range(6)])
