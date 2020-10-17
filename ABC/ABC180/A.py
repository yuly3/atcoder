import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, A, B = map(int, rl().split())
    print(N - A + B)


if __name__ == '__main__':
    solve()
