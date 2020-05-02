import sys
from math import floor

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    A, B, N = map(int, rl().split())
    
    if N < B:
        ans = floor(A * N / B) - A * floor(N / B)
    else:
        ans = floor(A * (B - 1) / B) - A * floor((B - 1) / B)
    print(ans)


if __name__ == '__main__':
    solve()
