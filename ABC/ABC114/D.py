import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if not arr:
        arr.append([n, 1])
    return arr


def solve():
    N = int(rl())
    
    counter = defaultdict(int)
    for x in range(1, N + 1):
        facts = factorization(x)
        for fact, exp in facts:
            counter[fact] += exp
    
    M = len(counter.keys())
    nums = tuple(counter.values())
    div75 = (1, 3, 5, 15, 25, 75)
    dp = [[0] * 76 for _ in range(M + 1)]
    dp[0][1] = 1
    for i in range(M):
        for div0 in div75:
            for div1 in div75:
                if div0 * div1 <= 75 and div1 <= nums[i] + 1:
                    dp[i + 1][div0 * div1] += dp[i][div0]
    print(dp[M][75])


if __name__ == '__main__':
    solve()
