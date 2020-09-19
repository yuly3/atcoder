import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    a, b, c, d = map(int, rl().split())
    ans = max(a * c, a * d, b * c, b * d)
    print(ans)


if __name__ == '__main__':
    solve()
