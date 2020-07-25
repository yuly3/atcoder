import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    X = int(rl())
    print(10 - X // 200)


if __name__ == '__main__':
    solve()
