import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    A, B = map(int, rl().split())
    print((2 * A + 100) - B)


if __name__ == '__main__':
    solve()
