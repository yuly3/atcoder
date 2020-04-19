import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    A = list(map(int, rl().split()))
    
    ans = N - sum(A)
    print(ans if 0 <= ans else -1)


if __name__ == '__main__':
    solve()
