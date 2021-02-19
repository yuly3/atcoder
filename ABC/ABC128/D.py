import sys
from heapq import heapify, heappop

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, K = map(int, rl().split())
    V = list(map(int, rl().split()))

    M = min(N, K)
    rV = list(reversed(V))
    ans = -(10 ** 10)
    for left in range(M + 1):
        for right in range(M + 1 - left):
            heapque = V[:left] + rV[:right]
            heapify(heapque)
            cnt = K - left - right
            while heapque and heapque[0] < 0 and 0 < cnt:
                heappop(heapque)
                cnt -= 1
            ans = max(ans, sum(heapque))
    print(ans)


if __name__ == '__main__':
    solve()
