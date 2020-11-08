import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    if N % 2 == 1:
        print('Black')
    else:
        print('White')


if __name__ == '__main__':
    solve()
