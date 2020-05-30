import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    L = [int(rl()) for _ in range(N)]
    
    cumsum = [0]
    for li in L:
        cumsum.append(cumsum[-1] + li)
    
    len_mins = []
    for i in range(N):
        for j in range(i + 1, N + 1):
            if i == 0 and j == N:
                break
            len_mins.append(cumsum[j] - cumsum[i])
    
    def check(t):
        for len_min in len_mins:
            len_max = len_min + t
            dp = [False] * (N + 1)
            dp[0] = True
            for left in range(N):
                if not dp[left]:
                    continue
                for right in range(left + 1, N + 1):
                    if left == 0 and right == N:
                        break
                    if len_min <= cumsum[right] - cumsum[left] <= len_max:
                        dp[right] = True
            if dp[-1]:
                return True
        return False
    
    ok, ng = 1000, -1
    while 1 < ok - ng:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == '__main__':
    solve()
