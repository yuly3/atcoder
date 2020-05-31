import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    A, B = map(int, rl().split())
    print(A * B)


if __name__ == '__main__':
    solve()
