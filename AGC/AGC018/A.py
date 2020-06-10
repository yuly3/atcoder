import sys
from fractions import gcd
from functools import reduce

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, K = map(int, rl().split())
    A = list(map(int, rl().split()))
    
    gcd_n = reduce(gcd, A)
    max_a = max(A)
    
    if K % gcd_n == 0 and K <= max_a:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')


if __name__ == '__main__':
    solve()
