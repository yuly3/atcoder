def solve():
    n, *a_l = map(int, open(0).read().split())
    l, r = 0, sum(a_l)
    d = r - l
    for i in range(n):
        l += a_l[i]
        r -= a_l[i]
        if d > abs(l - r):
            d = abs(l - r)

    print(d)


if __name__ == '__main__':
    solve()