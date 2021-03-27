import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    S = rl().rstrip()
    print(S[1:] + S[:1])


if __name__ == '__main__':
    solve()
