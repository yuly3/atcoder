import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, W = map(int, rl().split())
    print(N // W)


if __name__ == '__main__':
    solve()
