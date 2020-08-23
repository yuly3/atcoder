import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, X, T = map(int, rl().split())
    print(T * -(-N // X))


if __name__ == '__main__':
    solve()
