import sys

rl = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def solve():
    arr = list(map(int, rl().split()))
    arr.sort()
    print(arr[-3])


if __name__ == '__main__':
    solve()
