import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    MOD = 10 ** 9 + 7
    N = int(rl())
    ans = pow(10, N, MOD) - (2 * pow(9, N, MOD) - pow(8, N, MOD))
    ans %= MOD
    print(ans)


if __name__ == '__main__':
    solve()
