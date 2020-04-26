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
    MOD = 10 ** 9 + 7
    
    counter = defaultdict(int)
    for i in range(2, N + 1):
        facts = factorization(i)
        for j, cnt in facts:
            counter[j] += cnt
    
    ans = 1
    for val in counter.values():
        ans = ans * (val + 1) % MOD
    print(ans)


if __name__ == '__main__':
    solve()
