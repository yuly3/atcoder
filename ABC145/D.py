def cmb(n, r, mod):
    if r < 0 or n < r:
        return 0
    r = min(r, n-r)
    numerator, denominator = 1, 1
    for i in range(1, r + 1):
        numerator = (numerator * (n + 1 - i)) % mod
        denominator = (denominator * i) % mod
    return numerator * pow(denominator, mod - 2, mod) % mod


def solve():
    MOD = 10**9+7
    X, Y = map(int, input().split())

    if (X + Y) % 3 != 0:
        print(0)
        exit()
    
    n = (2 * Y - X) // 3
    m = (X - n) // 2
    
    if n < 0 or m < 0:
        print(0)
        exit()
    
    ans = cmb(n + m, n, MOD)
    print(ans)


if __name__ == '__main__':
    solve()