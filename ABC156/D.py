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
    n, a, b = map(int, input().split())
    MOD = 10 ** 9 + 7
    
    ans = pow(2, n, MOD) - 1
    ans -= cmb(n, a, MOD)
    ans -= cmb(n, b, MOD)
    print(ans % MOD)


if __name__ == '__main__':
    solve()
