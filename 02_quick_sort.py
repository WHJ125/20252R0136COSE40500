def qsort(a):
    if len(a) < 2: return a
    p = a[0]
    return qsort([x for x in a[1:] if x <= p]) + [p] + qsort([x for x in a[1:] if x > p])

print(qsort([3, 1, 4, 1, 5, 9]))
