import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    a, b = map(int, rl().split())
    c, d = map(int, rl().split())
    print(a * d - b * c)


if __name__ == '__main__':
    solve()
