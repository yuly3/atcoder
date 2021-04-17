import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    X, Y, Z = map(int, rl().split())
    t = Y * Z
    for i in range(10 ** 7, -1, -1):
        if i * X < t:
            print(i)
            return


if __name__ == '__main__':
    solve()
