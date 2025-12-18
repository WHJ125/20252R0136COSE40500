import heapq

g = {0:[(1,2),(2,5)], 1:[(2,1)], 2:[]}
dist = {0:0, 1:10**9, 2:10**9}
pq = [(0,0)]
while pq:
    d,v = heapq.heappop(pq)
    if d != dist[v]: continue
    for u,w in g[v]:
        nd = d + w
        if nd < dist[u]:
            dist[u] = nd
            heapq.heappush(pq, (nd,u))

print(dist)
