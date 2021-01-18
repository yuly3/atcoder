import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    X, Y = map(int, rl().split())
    if max(X, Y) - min(X, Y) < 3:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()
