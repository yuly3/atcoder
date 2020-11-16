import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    sx, sy, gx, gy = map(int, rl().split())
    print((gy * sx + sy * gx) / (sy + gy))


if __name__ == '__main__':
    solve()
