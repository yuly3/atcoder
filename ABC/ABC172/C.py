import sys
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M, K = map(int, rl().split())
    A = list(map(int, rl().split()))
    B = list(map(int, rl().split()))
    
    accA = [0] + list(accumulate(A))
    accB = list(accumulate(B))
    ans = 0
    for i, v in enumerate(accA):
        if K < v:
            break
        ans = max(ans, i + bisect_right(accB, K - v))
    print(ans)


if __name__ == '__main__':
    solve()
