def bsearch(a, x):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x: return mid
        lo, hi = (mid + 1, hi) if a[mid] < x else (lo, mid - 1)
    return -1

print(bsearch([1, 3, 5, 7, 9], 7))
