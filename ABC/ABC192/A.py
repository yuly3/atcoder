import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    X = int(rl())
    ans = 100 - (X - 100 * (X // 100))
    print(ans)


if __name__ == '__main__':
    solve()
