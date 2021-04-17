import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, P = map(int, rl().split())
    MOD = 10 ** 9 + 7
    
    ans = (P - 1) * pow(P - 2, N - 1, MOD) % MOD
    print(ans)


if __name__ == '__main__':
    solve()
