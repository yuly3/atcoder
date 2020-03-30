import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    X = int(rl())
    ans = 1000 * (X // 500)
    X -= ans // 2
    ans += 5 * (X // 5)
    print(ans)


if __name__ == '__main__':
    solve()
