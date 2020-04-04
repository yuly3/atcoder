import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, K = map(int, rl().split())
    if N % K == 0:
        print(0)
        exit()

    print(min(N % K, abs(N - K * (N // K + 1))))


if __name__ == '__main__':
    solve()
