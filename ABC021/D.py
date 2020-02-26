def cmb(n, r, mod):
    if r < 0 or n < r:
        return 0
    r = min(r, n - r)
    numerator, denominator = 1, 1
    for i in range(1, r + 1):
        numerator = (numerator * (n + 1 - i)) % mod
        denominator = (denominator * i) % mod
    return numerator * pow(denominator, mod - 2, mod) % mod


def solve():
    n, k = map(int, open(0).read().split())
    MOD = 10 ** 9 + 7
    ans = cmb(n - 1 + k, n - 1, MOD)
    print(ans)


if __name__ == '__main__':
    solve()
