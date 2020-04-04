import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    x, y, z = map(int, rl().split())
    print(z, x, y)


if __name__ == '__main__':
    solve()
