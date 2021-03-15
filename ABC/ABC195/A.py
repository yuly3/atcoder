import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    M, H = map(int, rl().split())
    print('Yes' if H % M == 0 else 'No')


if __name__ == '__main__':
    solve()
