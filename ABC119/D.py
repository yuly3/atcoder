from bisect import bisect_right


def solve():
    A, B, Q, *stx = map(int, open(0).read().split())
    INF = 10 ** 12
    s, t, x = [-INF] + stx[:A] + [INF], [-INF] + stx[A:A + B] + [INF], stx[A + B:]
    
    for xi in x:
        b, d = bisect_right(s, xi), bisect_right(t, xi)
        ans = INF
        for si in [s[b - 1], s[b]]:
            for ti in [t[d - 1], t[d]]:
                d1, d2 = abs(si - xi) + abs(ti - si), abs(ti - xi) + abs(si - ti)
                ans = min(ans, d1, d2)
        print(ans)


if __name__ == '__main__':
    solve()
