import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    a = int(rl())
    print(a + a ** 2 + a ** 3)


if __name__ == '__main__':
    solve()
