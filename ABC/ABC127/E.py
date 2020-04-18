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
    
    ans = 0
    for i in range(N):
        for j in range(M):
            tmp = (N - i) * (M - j) * (i + j) % MOD
            if i != 0 and j != 0:
                tmp *= 2
            ans = (ans + tmp) % MOD
    ans = ans * cmb(N * M - 2, K - 2) % MOD
    print(ans)


if __name__ == '__main__':
    solve()
