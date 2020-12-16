import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    a = list(map(int, rl().split()))
    print(min(a))


if __name__ == '__main__':
    solve()
