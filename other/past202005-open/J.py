import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    a = list(map(int, rl().split()))
    
    ans = [-1] * M
    highest = [0] * N
    for i in range(M):
        idx = bisect_left(highest, a[i]) - 1
        if idx != -1:
            highest[idx] = a[i]
            ans[i] = N - idx
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
