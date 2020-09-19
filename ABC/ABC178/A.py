import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    x = int(rl())
    print(x ^ 1)


if __name__ == '__main__':
    solve()
