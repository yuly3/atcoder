import sys
from math import gcd

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, Q = map(int, rl().split())
    A = list(map(int, rl().split()))
    S = list(map(int, rl().split()))
    
    for i in range(1, N):
        A[i] = gcd(A[i], A[i - 1])
    
    for si in S:
        if gcd(si, A[-1]) != 1:
            print(gcd(si, A[-1]))
            continue
        ok, ng = N - 1, -1
        while 1 < ok - ng:
            mid = (ok + ng) // 2
            if gcd(si, A[mid]) == 1:
                ok = mid
            else:
                ng = mid
        print(ok + 1)


if __name__ == '__main__':
    solve()
