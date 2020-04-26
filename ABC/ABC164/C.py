import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    kind = set()
    for _ in range(N):
        s = input()
        kind.add(s)
    print(len(kind))


if __name__ == '__main__':
    solve()
