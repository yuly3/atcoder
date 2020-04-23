import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    S = int(rl())
    x1, y1 = 0, 0
    x2, y2 = 1000000000, 1
    x3 = (x2 - S % x2) % x2
    y3 = (S + x3) // x2
    print('{} {} {} {} {} {}'.format(x1, y1, x2, y2, x3, y3))


if __name__ == '__main__':
    solve()
