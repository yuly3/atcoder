import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    S = rl().rstrip()
    if 'ooo' in S:
        print('o')
    elif 'xxx' in S:
        print('x')
    else:
        print('draw')


if __name__ == '__main__':
    solve()
