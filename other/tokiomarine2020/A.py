import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    S = rl().rstrip()
    print(S[:3])


if __name__ == '__main__':
    solve()
