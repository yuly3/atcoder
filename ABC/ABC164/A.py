import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    S, W = map(int, rl().split())
    if S <= W:
        print('unsafe')
    else:
        print('safe')


if __name__ == '__main__':
    solve()
