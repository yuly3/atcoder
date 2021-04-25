import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    A, B, C = map(int, rl().split())
    if A ** 2 + B ** 2 < C ** 2:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()
