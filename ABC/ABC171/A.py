import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    a = rl().rstrip()
    if a.isupper():
        print('A')
    else:
        print('a')


if __name__ == '__main__':
    solve()
