import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    _, _ = map(int, rl().split())
    a = list(map(int, rl().split()))
    
    max_a = max(a)
    d = sum(a) - max_a
    d = max_a - d
    print(max(0, d - 1))


if __name__ == '__main__':
    solve()
