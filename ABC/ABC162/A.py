import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = input()
    if '7' in N:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()
