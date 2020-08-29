import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    D, T, S = map(int, rl().split())
    if D / S <= T:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()
