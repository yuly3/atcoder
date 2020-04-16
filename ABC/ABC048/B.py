import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    a, b, x = map(int, rl().split())
    ans = b // x - a // x
    if a % x == 0:
        ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
