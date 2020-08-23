import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = rl().rstrip()
    N = sum(int(ni) for ni in N)
    print('Yes' if N % 9 == 0 else 'No')


if __name__ == '__main__':
    solve()
