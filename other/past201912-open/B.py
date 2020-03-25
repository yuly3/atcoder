import sys

rl = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def solve():
    N = int(rl())
    c = int(rl())
    for _ in range(N - 1):
        nx = int(rl())
        if c == nx:
            print('stay')
        elif nx < c:
            print('down', c - nx)
            c = nx
        else:
            print('up', nx - c)
            c = nx


if __name__ == '__main__':
    solve()
