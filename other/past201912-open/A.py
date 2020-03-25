import sys

rl = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def solve():
    S = input()
    if S.isdecimal():
        print(2 * int(S))
    else:
        print('error')


if __name__ == '__main__':
    solve()
