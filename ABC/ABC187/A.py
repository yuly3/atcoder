import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    AB = rl().rstrip()
    print(max(map(lambda n: sum(int(ni) for ni in n), AB.split())))


if __name__ == '__main__':
    solve()
