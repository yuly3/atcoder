import sys
from bisect import bisect_right

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
    
    if N == 1:
        print(0)
        return
    
    acc = [1]
    for i in range(2, 100):
        acc.append(acc[-1] + i)
    
    facts = factorization(N)
    ans = 0
    for fact, exp in facts:
        ans += bisect_right(acc, exp)
    print(ans)


if __name__ == '__main__':
    solve()
