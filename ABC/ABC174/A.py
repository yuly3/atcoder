import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    X = int(rl())
    if 30 <= X:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()
