import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def cmb(n, r, mod=10 ** 9 + 7):
    if r < 0 or n < r:
        return 0
    r = min(r, n - r)
    numerator, denominator = 1, 1
    for i in range(1, r + 1):
        numerator = (numerator * (n + 1 - i)) % mod
        denominator = (denominator * i) % mod
    return numerator * pow(denominator, mod - 2, mod) % mod


def solve():
    N, M, K = map(int, rl().split())
    MOD = 10 ** 9 + 7
    
    comb = cmb(N * M - 2, K - 2)
    ans = 0
    for d in range(1, N):
        cnt = d * (N - d) * M ** 2 % MOD
        cnt *= comb
        ans += cnt % MOD
        ans %= MOD
    for d in range(1, M):
        cnt = d * (M - d) * N ** 2 % MOD
        cnt *= comb
        ans += cnt % MOD
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    solve()
