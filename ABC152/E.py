from fractions import gcd


def solve():
    N, *A = map(int, open(0).read().split())
    MOD = 10 ** 9 + 7

    lcm = 1
    for a in A:
        lcm = a * lcm // gcd(a, lcm)

    ans = sum([lcm // a for a in A]) % MOD
    print(ans)


if __name__ == '__main__':
    solve()
