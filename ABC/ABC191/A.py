import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    V, T, S, D = map(int, rl().split())
    if T * V <= D <= S * V:
        print('No')
    else:
        print('Yes')


if __name__ == '__main__':
    solve()
