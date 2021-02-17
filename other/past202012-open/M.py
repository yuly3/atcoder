import sys
from collections import deque
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, L = map(int, rl().split())
    A = list(map(int, rl().split()))
    
    acc_A = list(accumulate(A))
    
    def check(t):
        dp = [False] * N
        que = deque([0])
        for i in range(N):
            while que:
                if que[0] + t <= acc_A[i] <= que[0] + L:
                    dp[i] = True
                    que.append(acc_A[i])
                    break
                if acc_A[i] < que[0] + t:
                    break
                que.popleft()
        return dp[-1]
    
    ok, ng = min(A), L + 1
    while ng - ok != 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == '__main__':
    solve()
