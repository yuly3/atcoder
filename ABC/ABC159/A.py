import sys
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    ans = N * (N - 1) // 2 + M * (M - 1) // 2
    print(ans)


if __name__ == '__main__':
    solve()
