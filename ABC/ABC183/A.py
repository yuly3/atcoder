import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    x = int(rl())
    print(x if 0 <= x else 0)


if __name__ == '__main__':
    solve()
